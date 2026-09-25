import os
from google import genai

# Initialize the GenAI client. 
# Requires the GEMINI_API_KEY environment variable to be set.
client = genai.Client()

def load_framework_docs():
    """Reads your Markdown playbooks to ground the model."""
    framework_text = ""
    # Map the specific files you want to load into the copilot's context
    docs = [
        "03_A_Ransomware_Playbook.md", 
        "03_B_Insider_Threat_Playbook.md",
        "03_C_Live_Triage_CheatSheet.md"
    ]
    
    for doc in docs:
        path = os.path.join("docs", doc)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                framework_text += f"\n--- {doc} ---\n{f.read()}"
        else:
            print(f"Warning: {doc} not found in /docs")
            
    return framework_text

def main():
    print("Loading DFIR playbooks into context...")
    playbooks = load_framework_docs()
    
    system_instruction = (
        "You are an Enterprise DFIR Copilot, an expert Incident Commander. "
        "Base all procedural advice strictly on the provided playbook files below. "
        "Provide step-by-step execution. Do not hallucinate external procedures.\n\n"
        f"{playbooks}"
    )
    
    print("\nDFIR Copilot Initialized (Gemini 3.8 Flash). Type 'quit' to exit.")
    
    while True:
        user_input = input("\n[Investigator] > ")
        if user_input.lower() in ['quit', 'exit']:
            break
            
        try:
            # Call the Interactions API to process the query against your playbooks
            interaction = client.interactions.create(
                model="gemini-3.8-flash",
                input=f"{system_instruction}\n\nInvestigator Update: {user_input}",
                # Enable Code Execution so the model can write Python to parse CSV logs if pasted
                tools=[{"type": "code_execution"}]
            )
            
            print(f"\n[DFIR Copilot]\n{interaction.output_text}")
            
        except Exception as e:
             print(f"\n[Error connecting to API]: {e}")

if __name__ == "__main__":
    main()

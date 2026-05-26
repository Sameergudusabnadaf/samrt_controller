from assistant import SamAssistant

def main():
    print("Starting Sam Assistant in Background Mode...")
    core = SamAssistant()
    
    # Run startup greeting
    core.startup()
    
    # Enter continuous listening loop
    core.run_continuously()

if __name__ == "__main__":
    main()

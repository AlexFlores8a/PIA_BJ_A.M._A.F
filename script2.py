import subprocess
import sys

def main():
    print("=== Ejecutando análisis completo (Script 2) ===\n")
    scripts = ["analysis.py", "visualizations.py", "datasheet.py"]
    for script in scripts:
        print(f"Ejecutando {script}...")
        result = subprocess.run([sys.executable, script], capture_output=False)
        if result.returncode != 0:
            print(f"❌ Error en {script}")
            break
        print("✅ Completado\n")
    print("🎉 Script 2 finalizado.")

if __name__ == "__main__":
    main()

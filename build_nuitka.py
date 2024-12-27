import os
import sys
from nuitka.Main import main

def compile_module():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the module to compile
    module_path = os.path.join(current_dir, 'models', 'elo_history_customer.py')
    
    # Nuitka compilation arguments
    args = [
        '--module',
        '--follow-import-to=odoo',  # Follow only odoo imports
        '--follow-import-to=models',  # Follow your models
        '--no-pyi-file',  # Don't generate .pyi files
        '--static-libpython=no',
        module_path
    ]
    
    # Run Nuitka compilation
    sys.argv.extend(args)
    main()

if __name__ == '__main__':
    compile_module()
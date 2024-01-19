import argparse
import pandas as pd

def main():
    
    parser = argparse.ArgumentParser(description='Aplicación de consola que imprime argumentos')

    parser.add_argument('--arg1', default='valor1', help='Descripción del argumento 1')
    parser.add_argument('--arg2', default='valor2', help='Descripción del argumento 2')
    parser.add_argument('--arg3', default='valor3', help='Descripción del argumento 3')

    args = parser.parse_args()

    print(f'Argumento 1: {args.arg1}')
    print(f'Argumento 2: {args.arg2}')
    print(f'Argumento 3: {args.arg3}')

if __name__ == '__main__':
    main()

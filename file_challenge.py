# File Read & Write Challenge + Error Handling Lab

def process_line(line):
    """
    Função para modificar cada linha do arquivo.
    Aqui, como exemplo, vamos colocar tudo em maiúsculas.
    """
    return line.upper()


def main():
    try:
        # Perguntar ao usuário o nome do arquivo de entrada
        input_filename = input("Enter the name of the file to read: ")

        # Abrir o arquivo para leitura
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Criar nome do arquivo de saída
        output_filename = "modified_" + input_filename

        # Abrir arquivo de saída e escrever as linhas processadas
        with open(output_filename, 'w') as outfile:
            for line in lines:
                modified_line = process_line(line)
                outfile.write(modified_line)

        print(f"File has been processed successfully! Modified file: {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

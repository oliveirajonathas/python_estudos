try:
    a = int(input('Numerador: '))
    b = int(input('Denominador '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível divisão por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volta sempre! Muito obrigado!')

def run(_char):
    '''
    英大文字か英小文字のいずれか 1 文字 α が入力されます。 α が英大文字なら A、英小文字なら a と出力してください。
    '''
    print('A' if str.isupper(_char) else 'a')

if __name__ == '__main__':
    _char = input()
    run(_char)
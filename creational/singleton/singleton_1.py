"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""

class AppSettings(
    object
):
    __instance = None
    
    def __new__(cls , *args , **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls,*args , **kwargs)
            
        return cls.__instance

    
if __name__ == "__main__":
    settings_1 = AppSettings()
    settings_2 = AppSettings()
    
    print(settings_1 == settings_2)
    print(id(settings_1) == id(settings_2))
    
    settings_1.port = 800
    
    print(settings_2.port)
from subtitles.subtitles import get_subtitles, parse_srt_string, group_subtitle_texts
from database.database import initialize_database, add_to_collection



client = initialize_database()

def main_flow():


    print("Este é um ChatBot feito para responder perguntas sobre podcasts!\n O usuário pode fornecer um podcast por meio da URL do Youtube")
    print("Este bot trabalha com a legenda do podcast, verifique se há legendas no podcast. No momento as legendas são em portugues\n")


    while True:

        print("Deseja fazer:\n1. Pergunta\n2. Adicionar um podcast\nX. digite \"n\" para sair.\n")
        choice = input("-> ")

        if(choice == "n"):
            break
        elif choice == "1":
            pass
        elif choice == "2":
            url = input("Qual URL do podcast?\n-> ")
            add_podcast(url=url)
        else:
            print("Escolha uma opção válida.\n")

def add_podcast(url):
    podcast_dict = get_subtitles(url=url)
    add_to_collection(podcast_dict,client=client)
    

    
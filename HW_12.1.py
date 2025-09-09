# ДЗ 12.1. Очистити текст від html-тегів


import codecs 


def delete_html_tags(html_file, result_file='cleaned.txt'): 
      with codecs.open(html_file, 'r', 'utf-8') as file: 
            html = file.read()

      # while all(["<" in html, ">" in html]):   Цей алгоритм видаляє теги разом із їхнім вмістом, але при переписуванні в інший файл, весь текст знаходиться в одній строці
                 
      #      for i in html:
                        
      #             if i in "<":
      #                  state = True
      #             elif i in ">":
      #                   html = html.replace(i, " ")
      #                   state = False

      #             if state:
      #                   html = html.replace(i, " ")


      lst = []

      # переписує текст, що знаходиться поза межами тегів
      for i in html:
                        
            if i in "<":
                  state = False

            elif i in ">":
                  state = True
                  continue

            if state:
                  lst.append(i)



      without_tags = "".join(lst)

      # print(without_tags)
                        
                      
      with codecs.open(result_file, "w", "utf-8") as file:
            file.write(without_tags)

   


delete_html_tags("draft.html", "text.txt")

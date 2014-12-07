# -*- coding: cp1252 -*-
from xml.dom import minidom
doc = minidom.parse('C:\Users\SAM\Documents\QLC\merger\scenes lyre.qxw')
doc = minidom.parse('C:\Users\SAM\Documents\QLC\merger\scenebig.qxw')

root = doc.documentElement
current = root.firstChild

sequence=False
num_scene=0

for engine_node in root.getElementsByTagName('Engine'):
     #print engine_node
     node = engine_node.firstChild
     for fixture_node in engine_node.getElementsByTagName('Fixture'):
         print "====Fixture===="
         for prop_fixture in fixture_node.childNodes:
             #print "test=>",prop_fixture.nodeName
             if prop_fixture.nodeName != "#text":
                 #nom de l'attribut
                 print ">>",prop_fixture.nodeName,prop_fixture.firstChild.nodeValue

     for function_node in engine_node.getElementsByTagName('Function'):
         #Liste des fonctions: EFX(concerne les lyre pointe vers une fixture)
         #                     Scene
         #                     Chaser
         #                     RGBMatrix
         #                     Collection

         print "====Fonction===="
         #RECUP PROPRIETE DES FONCTIONS
         if "Path" in function_node.attributes.keys():
             #LES FONCTION SCENE POSSEDE EN PLUS UN PATH
             f_path=function_node.attributes.values()[0].nodeValue
             f_type=function_node.attributes.values()[1].nodeValue
             f_name=function_node.attributes.values()[2].nodeValue
             f_ID=function_node.attributes.values()[3].nodeValue
         else:
             f_type=function_node.attributes.values()[0].nodeValue
             f_name=function_node.attributes.values()[1].nodeValue
             f_ID=function_node.attributes.values()[2].nodeValue

         if f_type == "EFX":
             #TRAITEMENT DE EFX
             print "    ====EFX====",f_type,f_name,f_ID
             #descente dans le child pour lire props de la fonction
             for props_funtion in  function_node.childNodes:
                 #print props_funtion.nodeName
                 if props_funtion.nodeName != "#text":
                     #nom de l'attribut
                     print ">>",props_funtion.nodeName
                     
         if f_type == "Scene":
             #TRAITEMENT DE SCENE
             print "    ====Scene====",f_path,f_type,f_name,f_ID
             #descente dans lechild pour lire props de la fonction
             for props_funtion in  function_node.childNodes:
                 if props_funtion.nodeName == "Speed":
                     FadeOut=props_funtion.attributes.values()[0].nodeValue
                     FadeIn=props_funtion.attributes.values()[1].nodeValue
                     Duration=props_funtion.attributes.values()[2].nodeValue
                     print '<Speed FadeOut="%s" FadeIn="%s" Duration="%s"/>'%(FadeOut,FadeIn,Duration)

                 if props_funtion.nodeName == "FixtureVal":
                     ID=props_funtion.attributes.values()[0].nodeValue
                     print '<FixtureVal ID="%s">%s</FixtureVal>'%(ID,props_funtion.firstChild.nodeValue)
                    
        
         if f_type == "Chaser":
             #TRAITEMENT DE CHASER
             print "    ====Chaser====",f_type,f_name,f_ID
             #descente dans lechild pour lire props de la fonction
             for props_funtion in  function_node.childNodes:
                 if props_funtion.nodeName == "Speed":
                     FadeOut=props_funtion.attributes.values()[1].nodeValue
                     FadeIn=props_funtion.attributes.values()[2].nodeValue
                     Duration=props_funtion.attributes.values()[0].nodeValue
                     print '<Speed FadeOut="%s" FadeIn="%s" Duration="%s"/>'%(FadeOut,FadeIn,Duration)

                 if props_funtion.nodeName == "Direction":
                     print '<Direction>%s</Direction>'%(props_funtion.firstChild.nodeValue)
                     
                 if props_funtion.nodeName == "RunOrder":
                     print '<RunOrder>%s</RunOrder>'%(props_funtion.firstChild.nodeValue)
                     
                 if props_funtion.nodeName == "SpeedModes":
                     FadeOut=props_funtion.attributes.values()[1].nodeValue
                     FadeIn=props_funtion.attributes.values()[2].nodeValue
                     Duration=props_funtion.attributes.values()[0].nodeValue
                     print '<SpeedModes FadeOut="%s" FadeIn="%s" Duration="%s"/>'%(FadeOut,FadeIn,Duration)
                     
                 if props_funtion.nodeName == "Sequence":
                     sequence=True
                     #DANS LE CAS D'UNE SEQUENCE ET NON UN CHASER PUR
                     BoundScene=props_funtion.attributes.values()[0].nodeValue
                     print '<Sequence BoundScene="%s"/>'%(BoundScene)
                     
                 if props_funtion.nodeName == "Step":
                     if sequence:
                         Number=props_funtion.attributes.values()[3].nodeValue
                         Values=props_funtion.attributes.values()[2].nodeValue
                         FadeOut=props_funtion.attributes.values()[0].nodeValue
                         Hold=props_funtion.attributes.values()[1].nodeValue
                         FadeIn=props_funtion.attributes.values()[4].nodeValue
                         print '<Step Number="%s" Values="%s" FadeOut="%s" Hold="%s" FadeIn="%s"/>'%(Number,Values,FadeOut,Hold,FadeIn)

                     else:
                         Number=props_funtion.attributes.values()[2].nodeValue
                         FadeOut=props_funtion.attributes.values()[0].nodeValue
                         Hold=props_funtion.attributes.values()[1].nodeValue
                         FadeIn=props_funtion.attributes.values()[3].nodeValue
                         print '<Step Number="%s" FadeOut="%s" Hold="%s" FadeIn="%s">%s</Step>'%(Number,FadeOut,Hold,FadeIn,props_funtion.firstChild.nodeValue)
                         
                         
             sequence=False

         if f_type == "RGBMatrix":
             #TRAITEMENT DE RGBMatrix
             print "    ====RGBMatrix====",f_type,f_name,f_ID
             #descente dans lechild pour lire props de la fonction
             for props_funtion in  function_node.childNodes:
                 #print props_funtion.nodeName
                 if props_funtion.nodeName != "#text":
                     #nom de l'attribut
                     print ">>",props_funtion.nodeName

         if f_type == "Collection":
             #TRAITEMENT DE Collection
             print "    ====Collection====",f_type,f_name,f_ID
             #descente dans lechild pour lire props de la fonction
             for props_funtion in  function_node.childNodes:
                 #print props_funtion.nodeName
                 if props_funtion.nodeName != "#text":
                     #nom de l'attribut
                     print ">>",props_funtion.nodeName
                     



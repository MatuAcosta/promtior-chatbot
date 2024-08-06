# Chatbot - Challenge - Promtior

Este proyecto consiste de un chatbot que permite al usuario conocer más y preguntar dudas acerca de Promtior a través de la implementación de la arquitectura RAG.

## Objetivo

Desarrollar y desplegar un chatbot que a través de la implementación de la arquitectura RAG pueda responder preguntas acerca del contenido del Sitio Web de Promtior, utilizando la libreria LangCHain.
El chatbot debe poder responder las siguientes preguntas: 
### What services does Promtior offer?
### When was the company founded?


## Desafíos

### 1. **Adentrarme en el mundo de la IA y RAG**
   #### Mucha lectura de documentación y algún que otro video para poder entender el funcionamiento de la arquitectura RAG y los diferentes componentes que se pueden encontrar dentro de esta como los vectorstores, LLM, etc. La verdad que es un mundo apasionante y que parece que nunca se termina de aprender.

### 2.**Presentación del chat**
   #### Decidí avanzar por lo simple y conciso desplegando archivos estaticos gracias a la ayuda de FastAPI.

### 3. **Despliegue en AWS**
   ### Al no tener mucha experiencia utilizando estos servicios cloud, es una buena oportunidad para poder utilizarlos y poder aprender algo.



## Problemas Encontrados y Soluciones

### 1. **Falta de algunos datos en el Sitio web**
   - **Descripción**: Al realizar una investigacion me di cuenta que el sitio web solamente no ofrece información acerca de cuando se fundó la compañia, por lo cual el chatbot respondia que no conocia la fecha de fundación. Además no sabia como unir 2 fuentes de información diferente.
   - **Solución**: Utilicé datos la presentación brindada en el mail del challenge y agregué a los vector stores para que así el modelo pueda saber que responder ante dicha pregunta.

### 2. **Ajustes de CORS**
   - **Descripción**: Tipicos problemas de cors.
   - **Solución**: Fueron solucionados rapidamente pero suelen ser un dolor de cabeza.

## Link de acceso
   ###  http://34.228.140.169/ 

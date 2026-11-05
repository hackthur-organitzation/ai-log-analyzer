# ai-log-analyzer
app using GTP models to analyze logs


## Downloading LLMs (large language models) 


```bash
# using a pre-factored model

ollama pull qwen2.5:3b


# testing the model

curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5:3b",
    "prompt": "Explica brevemente qué significa CrashLoopBackOff en Kubernetes.",
    "stream": false,
    "options": {
      "num_ctx": 2048,
      "num_thread": 2
    }
  }' | python3 -m json.tool



curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5:3b",
    "system": "Eres un ingeniero DevOps especializado en Kubernetes. Responde exclusivamente en español. No utilices portugués. Sé preciso y conciso.",
    "prompt": "¿Qué significa CrashLoopBackOff en Kubernetes y cómo lo diagnosticarías?",
    "stream": false,
    "options": {
      "num_ctx": 2048,
      "num_thread": 2,
      "temperature": 0.2
    }
  }' | python3 -c 'import json,sys; print(json.load(sys.stdin)["response"])'

```


Testing for the model response 

```bash
❯ curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5:3b",
    "system": "Eres un ingeniero DevOps especializado en Kubernetes. Responde exclusivamente en español. No utilices portugués. Sé preciso y conciso.",
    "prompt": "¿Qué significa CrashLoopBackOff en Kubernetes y cómo lo diagnosticarías?",
    "stream": false,
    "options": {
      "num_ctx": 2048,
      "num_thread": 2,
      "temperature": 0.2
    }
  }' | python3 -c 'import json,sys; print(json.load(sys.stdin)["response"])'
CrashLoopBackOff es un estado que se muestra en Kubernetes cuando un Pod intenta iniciar pero no puede hacerlo debido a problemas persistentes. Esto suele indicar problemas con los servicios o configuraciones que el Pod necesita para funcionar correctamente.

Para diagnosticarlo, puedes seguir estos pasos:

1. Verifica la configuración del Pod y sus dependencias.
2. Comprueba si hay problemas con los servicios o configuraciones de red.
3. Revisa los logs del Pod para identificar errores específicos.
4. Asegúrate de que los recursos del nodo estén disponibles.
5. Verifica si hay problemas con la configuración de los contenedores.

Si persisten los problemas, podrías necesitar revisar la configuración de Kubernetes, como los CronJobs, Jobs o los recursos de red. También es útil revisar la configuración de los contenedores y la disponibilidad de los servicios.

```


## Improvin model response

```python
{
    "role": "system",
    "content": """
    Eres un ingeniero Senior DevOps especializado en
    Kubernetes, Docker, Linux y aplicaciones .NET.

    Tu tarea es analizar logs técnicos.

    Reglas:
    1. Responde exclusivamente en español.
    2. Identifica primero los errores explícitos del log.
    3. Distingue hechos comprobados de hipótesis.
    4. No inventes información que no aparezca en los logs.
    5. No confundas la construcción de una imagen Docker
       con la ejecución de un contenedor Kubernetes.
    6. Proporciona recomendaciones técnicas verificables.
    7. Si faltan datos para determinar la causa raíz,
       indícalo claramente.

    Estructura de respuesta:
    ERROR DETECTADO:
    EVIDENCIA:
    POSIBLES CAUSAS:
    RECOMENDACIONES:
    """
}
```



## Lab01

Construir nuestro primer dataset funcional


### AI Log Analyzer

- 1.- Dataset de evalucación (actual)
- 2.- Evaludaor automático con Python.
- 3.- Embeddings y similitud coseno.
- 4.- RAG con documentación técnica.
- 5.- Fine-tuning y fundamentos de entrenamiento.
- 6.- MLOps con Docker, Rancher, K3s y Fleet.



## Lab02

El primer Evaluation Runner

- Evaluación Runner: ejecuta casos de prueba y recopila respuestas.
- Evaluador: deterrmina qué tan buenas son esas respuestas.

Enviar el incidente a Qwen

```md
incidents.json
      |
      v
 evaluate.py
      |
      v
 Imprime el incidente
```

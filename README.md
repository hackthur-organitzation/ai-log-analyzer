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
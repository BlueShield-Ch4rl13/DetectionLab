# 🟣 Mapeo Purple Team — Atomic Red Team ↔ Detecciones

<!-- Generado por tools/build.py — no editar a mano · fuente: rules/ -->

El bucle: **emular** una técnica con Atomic Red Team → comprobar que **salta**
la regla en el SIEM → si no salta, **afinar** la regla → volver a medir la
cobertura.

Este fichero **se genera** desde `rules/` con `python tools/build.py`. No se
edita a mano: un mapa que cita reglas que ya no existen manda a emular una
técnica y luego a buscar una detección que nadie va a disparar.

> Ejecuta las pruebas **solo en el laboratorio aislado**. Limpia siempre con
> `-Cleanup`.

## Estado

| | Reglas |
|---|---|
| En el repositorio | 127 |
| Con una técnica ATT&CK que se puede emular con Atomic Red Team | 122 |
| Probadas con Atomic y resultado registrado en `purple/resultados.csv` | 0 |
| De ellas, detectadas | 0 |

Tener técnica a emular no es estar validada: solo cuenta como validada una
regla con una ejecución real registrada en `resultados.csv`.

```powershell
Install-Module -Name Invoke-AtomicRedTeam -Scope CurrentUser
Import-Module Invoke-AtomicRedTeam
Invoke-AtomicTest T1003.001                 # ejecuta la tecnica
Invoke-AtomicTest T1003.001 -Cleanup        # revierte
```

## Windows — Sysmon y canal Security

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1003 | `Invoke-AtomicTest T1003` | ⬜ `soc_ad_005_herramientas_kerberos` | Sysmon EID 1 |
| T1003.001 | `Invoke-AtomicTest T1003.001` | ⬜ `cred_004_descenso_wdigest`<br>⬜ `soc_edr_001_volcado_lsass`<br>⬜ `soc_edr_002_acceso_lsass_sysmon` | Sysmon EID 12/13/14 |
| T1003.002 | `Invoke-AtomicTest T1003.002` | ⬜ `cred_001_volcado_colmenas_registro` | Sysmon EID 1 |
| T1003.003 | `Invoke-AtomicTest T1003.003` | ⬜ `ad_018_extraccion_ntds` | Sysmon EID 1 |
| T1003.004 | `Invoke-AtomicTest T1003.004` | ⬜ `cred_001_volcado_colmenas_registro`<br>⬜ `cred_003_abuso_dpapi` | Sysmon EID 1 |
| T1003.005 | `Invoke-AtomicTest T1003.005` | ⬜ `cred_007_credenciales_cacheadas_vault` | Sysmon EID 1 |
| T1003.006 | `Invoke-AtomicTest T1003.006` | ⬜ `soc_ad_003_dcsync` | Canal Security / System de Windows |
| T1021.006 | `Invoke-AtomicTest T1021.006` | ⬜ `soc_ad_009_wmi_winrm_remoto` | Sysmon EID 1 |
| T1027 | `Invoke-AtomicTest T1027` | ⬜ `soc_edr_006_powershell_ofuscado` | Sysmon EID 1 |
| T1047 | `Invoke-AtomicTest T1047` | ⬜ `proc_wmic_process_call_create`<br>⬜ `soc_ad_009_wmi_winrm_remoto` | Sysmon EID 1 |
| T1053.005 | `Invoke-AtomicTest T1053.005` | ⬜ `soc_edr_008_persistencia_tarea` | Sysmon EID 1 |
| T1055 | `Invoke-AtomicTest T1055` | ⬜ `soc_edr_010_inyeccion_procesos` | Sysmon EID 8 |
| T1059.001 | `Invoke-AtomicTest T1059.001` | ⬜ `soc_edr_006_powershell_ofuscado` | Sysmon EID 1 |
| T1069.002 | `Invoke-AtomicTest T1069.002` | ⬜ `soc_ad_007_enumeracion_dominio` | Sysmon EID 1 |
| T1070.001 | `Invoke-AtomicTest T1070.001` | ⬜ `soc_edr_004_defensas_deshabilitadas` | Sysmon EID 1 |
| T1071 | `Invoke-AtomicTest T1071` | ⬜ `soc_edr_011_pipe_c2` | Sysmon EID 17/18 |
| T1071.001 | `Invoke-AtomicTest T1071.001` | ⬜ `net_rare_process_external_conn` | Sysmon EID 3 |
| T1087.002 | `Invoke-AtomicTest T1087.002` | ⬜ `ad_017_lectura_laps`<br>⬜ `soc_ad_007_enumeracion_dominio` | Sysmon EID 1 |
| T1098 | `Invoke-AtomicTest T1098` | ⬜ `ad_015_delegacion_kerberos`<br>⬜ `ad_016_adminsdholder` | Canal Security / System de Windows |
| T1105 | `Invoke-AtomicTest T1105` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1112 | `Invoke-AtomicTest T1112` | ⬜ `cred_004_descenso_wdigest` | Sysmon EID 12/13/14 |
| T1134.005 | `Invoke-AtomicTest T1134.005` | ⬜ `ad_014_sid_history` | Canal Security / System de Windows |
| T1136.001 | `Invoke-AtomicTest T1136.001` | ⬜ `proc_net_user_add` | Sysmon EID 1 |
| T1136.002 | `Invoke-AtomicTest T1136.002` | ⬜ `soc_ad_011_cuenta_equipo_creada` | Canal Security / System de Windows |
| T1140 | `Invoke-AtomicTest T1140` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1187 | `Invoke-AtomicTest T1187` | ⬜ `ad_019_coercion_ntlm` | Canal Security / System de Windows |
| T1197 | `Invoke-AtomicTest T1197` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1204.002 | `Invoke-AtomicTest T1204.002` | ⬜ `proc_office_spawning_shell`<br>⬜ `soc_edr_012_ejecucion_desde_temp` | Sysmon EID 1 |
| T1207 | `Invoke-AtomicTest T1207` | ⬜ `ad_013_dcshadow` | Canal Security / System de Windows |
| T1218 | `Invoke-AtomicTest T1218` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1218.005 | `Invoke-AtomicTest T1218.005` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1218.010 | `Invoke-AtomicTest T1218.010` | ⬜ `soc_edr_005_lolbins_descarga` | Sysmon EID 1 |
| T1222 | `Invoke-AtomicTest T1222` | ⬜ `ad_016_adminsdholder` | Canal Security / System de Windows |
| T1484.001 | `Invoke-AtomicTest T1484.001` | ⬜ `soc_ad_010_abuso_gpo` | Sysmon EID 1 |
| T1486 | `Invoke-AtomicTest T1486` | ⬜ `soc_edr_007_cifrado_masivo` | Sysmon EID 11 |
| T1490 | `Invoke-AtomicTest T1490` | ⬜ `soc_edr_003_borrado_copias_sombra` | Sysmon EID 1 |
| T1539 | — Robo de token de sesion: requiere un proxy AitM tipo Evilginx en laboratorio aislado | ⬜ `cred_002_credenciales_navegador` | Sysmon EID 1 |
| T1543.003 | `Invoke-AtomicTest T1543.003` | ⬜ `proc_service_create_scexe` | Sysmon EID 1 |
| T1547.001 | `Invoke-AtomicTest T1547.001` | ⬜ `soc_edr_009_persistencia_registro` | Sysmon EID 12/13/14 |
| T1550.002 | `Invoke-AtomicTest T1550.002` | ⬜ `soc_ad_006_pass_the_hash` | Canal Security / System de Windows |
| T1550.003 | `Invoke-AtomicTest T1550.003` | ⬜ `ad_015_delegacion_kerberos` | Canal Security / System de Windows |
| T1552.001 | `Invoke-AtomicTest T1552.001` | ⬜ `cred_005_credenciales_nube_ssh` | Sysmon EID 1 |
| T1552.004 | `Invoke-AtomicTest T1552.004` | ⬜ `cred_005_credenciales_nube_ssh` | Sysmon EID 1 |
| T1555 | `Invoke-AtomicTest T1555` | ⬜ `ad_017_lectura_laps`<br>⬜ `cred_003_abuso_dpapi` | Sysmon EID 1 |
| T1555.003 | `Invoke-AtomicTest T1555.003` | ⬜ `cred_002_credenciales_navegador` | Sysmon EID 1 |
| T1555.004 | `Invoke-AtomicTest T1555.004` | ⬜ `cred_007_credenciales_cacheadas_vault` | Sysmon EID 1 |
| T1555.005 | `Invoke-AtomicTest T1555.005` | ⬜ `cred_006_gestores_contrasenas` | Sysmon EID 1 |
| T1557.001 | `Invoke-AtomicTest T1557.001` | ⬜ `ad_019_coercion_ntlm` | Canal Security / System de Windows |
| T1558 | `Invoke-AtomicTest T1558` | ⬜ `soc_ad_005_herramientas_kerberos` | Sysmon EID 1 |
| T1558.001 | `Invoke-AtomicTest T1558.001` | ⬜ `soc_ad_004_golden_ticket` | Canal Security / System de Windows |
| T1558.003 | `Invoke-AtomicTest T1558.003` | ⬜ `soc_ad_001_kerberoasting` | Canal Security / System de Windows |
| T1558.004 | `Invoke-AtomicTest T1558.004` | ⬜ `soc_ad_002_asrep_roasting` | Canal Security / System de Windows |
| T1562.001 | `Invoke-AtomicTest T1562.001` | ⬜ `soc_edr_004_defensas_deshabilitadas` | Sysmon EID 1 |
| T1566.001 | — Entrega de phishing: se emula enviando un correo de prueba al tenant | ⬜ `proc_office_spawning_shell` | Sysmon EID 1 |
| T1569.002 | `Invoke-AtomicTest T1569.002` | ⬜ `soc_ad_008_psexec_remoto` | Canal Security / System de Windows |
| T1649 | `Invoke-AtomicTest T1649` | ⬜ `soc_ad_012_abuso_adcs` | Sysmon EID 1 |

## Linux — Sysmon for Linux

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1003.008 | `Invoke-AtomicTest T1003.008` | ⬜ `lin_read_shadow` | execve (auditd / Falco) |
| T1053.003 | `Invoke-AtomicTest T1053.003` | ⬜ `lin_cron_persistence` | execve (auditd / Falco) |
| T1059.004 | `Invoke-AtomicTest T1059.004` | ⬜ `lin_base64_decode_exec`<br>⬜ `lin_download_pipe_shell`<br>⬜ `lin_reverse_shell` | execve (auditd / Falco) |
| T1070.003 | `Invoke-AtomicTest T1070.003` | ⬜ `lin_disable_history` | execve (auditd / Falco) |
| T1098.004 | `Invoke-AtomicTest T1098.004` | ⬜ `lin_ssh_authorized_keys` | execve (auditd / Falco) |
| T1105 | `Invoke-AtomicTest T1105` | ⬜ `lin_download_pipe_shell` | execve (auditd / Falco) |
| T1136.001 | `Invoke-AtomicTest T1136.001` | ⬜ `lin_useradd` | execve (auditd / Falco) |
| T1140 | `Invoke-AtomicTest T1140` | ⬜ `lin_base64_decode_exec` | execve (auditd / Falco) |
| T1222.002 | `Invoke-AtomicTest T1222.002` | ⬜ `lin_chmod_tmp_exec` | execve (auditd / Falco) |
| T1574.006 | `Invoke-AtomicTest T1574.006` | ⬜ `lin_ld_preload` | execve (auditd / Falco) |

## macOS — Endpoint Security Framework

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1059.002 | `Invoke-AtomicTest T1059.002` | ⬜ `mac_osascript_sospechoso` | ESF exec |
| T1059.004 | `Invoke-AtomicTest T1059.004` | ⬜ `mac_descarga_y_ejecucion` | ESF exec |
| T1070.002 | `Invoke-AtomicTest T1070.002` | ⬜ `mac_borrado_de_registros` | ESF exec |
| T1070.003 | `Invoke-AtomicTest T1070.003` | ⬜ `mac_borrado_de_registros` | ESF exec |
| T1105 | `Invoke-AtomicTest T1105` | ⬜ `mac_descarga_y_ejecucion` | ESF exec |
| T1136.001 | `Invoke-AtomicTest T1136.001` | ⬜ `mac_usuario_oculto_creado` | ESF exec |
| T1543.001 | `Invoke-AtomicTest T1543.001` | ⬜ `mac_persistencia_launchagent` | ESF create |
| T1543.004 | `Invoke-AtomicTest T1543.004` | ⬜ `mac_persistencia_launchagent` | ESF create |
| T1548.006 | `Invoke-AtomicTest T1548.006` | ⬜ `mac_tcc_manipulacion` | ESF exec |
| T1553.001 | `Invoke-AtomicTest T1553.001` | ⬜ `mac_gatekeeper_deshabilitado` | ESF exec |
| T1555.001 | `Invoke-AtomicTest T1555.001` | ⬜ `mac_volcado_llavero` | ESF exec |
| T1562.001 | `Invoke-AtomicTest T1562.001` | ⬜ `mac_gatekeeper_deshabilitado` | ESF exec |

## Contenedores — auditoría de Kubernetes y runtime

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1078.003 | `Invoke-AtomicTest T1078.003` | ⬜ `k8s_escalada_por_rolebinding` | Auditoria del API server |
| T1552.007 | `Invoke-AtomicTest T1552.007` | ⬜ `k8s_lectura_masiva_secretos` | Auditoria del API server |
| T1609 | `Invoke-AtomicTest T1609` | ⬜ `k8s_exec_en_pod` | Auditoria del API server |
| T1610 | `Invoke-AtomicTest T1610` | ⬜ `cont_socket_runtime_accedido`<br>⬜ `k8s_pod_privilegiado` | execve (auditd / Falco) |
| T1611 | `Invoke-AtomicTest T1611` | ⬜ `cont_escape_a_namespaces_host`<br>⬜ `cont_socket_runtime_accedido`<br>⬜ `k8s_capacidades_peligrosas`<br>⬜ `k8s_montaje_hostpath`<br>⬜ `k8s_pod_privilegiado` | execve (auditd / Falco) |

## Nube e identidad — Entra ID, M365, CASB

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1078.004 | `Invoke-AtomicTest T1078.004` | ⬜ `soc_cld_009_dispositivo_no_conforme` | Entra ID (SigninLogs / AuditLogs) |
| T1090.003 | `Invoke-AtomicTest T1090.003` | ⬜ `soc_cld_008_origen_anonimizado` | Entra ID (SigninLogs / AuditLogs) |
| T1098.001 | `Invoke-AtomicTest T1098.001` | ⬜ `soc_cld_007_credencial_service_principal` | Entra ID (SigninLogs / AuditLogs) |
| T1098.003 | `Invoke-AtomicTest T1098.003` | ⬜ `soc_cld_005_rol_privilegiado` | Entra ID (SigninLogs / AuditLogs) |
| T1098.005 | `Invoke-AtomicTest T1098.005` | ⬜ `soc_cld_002_metodo_mfa_registrado` | Entra ID (SigninLogs / AuditLogs) |
| T1110.003 | — Rociado de contrasenas contra el IdP: usar una prueba controlada del propio tenant | ⬜ `soc_cld_003_password_spraying` | Entra ID (SigninLogs / AuditLogs) |
| T1528 | `Invoke-AtomicTest T1528` | ⬜ `soc_cld_001_consentimiento_oauth` | Entra ID (SigninLogs / AuditLogs) |
| T1539 | — Robo de token de sesion: requiere un proxy AitM tipo Evilginx en laboratorio aislado | ⬜ `soc_cld_004_token_robado` | Entra ID (SigninLogs / AuditLogs) |
| T1556.009 | `Invoke-AtomicTest T1556.009` | ⬜ `soc_cld_006_acceso_condicional` | Entra ID (SigninLogs / AuditLogs) |
| T1567.002 | `Invoke-AtomicTest T1567.002` | ⬜ `soc_cld_010_saas_no_aprobado` | Alertas de Netskope |

## Correo — Proofpoint TAP y Exchange Online

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1027.006 | `Invoke-AtomicTest T1027.006` | ⬜ `soc_mail_008_html_smuggling` | Proofpoint TAP |
| T1114.003 | `Invoke-AtomicTest T1114.003` | ⬜ `soc_mail_006_regla_buzon_externa` | Registro de auditoria de M365 |
| T1534 | — Envio interno masivo: se emula desde el propio buzon, no con Atomic | ⬜ `soc_mail_002_suplantacion_directivo`<br>⬜ `soc_mail_007_envio_masivo_interno` | Proofpoint TAP |
| T1564.008 | `Invoke-AtomicTest T1564.008` | ⬜ `soc_mail_006_regla_buzon_externa` | Registro de auditoria de M365 |
| T1566.001 | — Entrega de phishing: se emula enviando un correo de prueba al tenant | ⬜ `soc_mail_004_adjunto_sospechoso` | Proofpoint TAP |
| T1566.002 | `Invoke-AtomicTest T1566.002` | ⬜ `soc_mail_001_dominio_reciente`<br>⬜ `soc_mail_003_fallo_dmarc`<br>⬜ `soc_mail_005_url_pulsada` | Proofpoint TAP |

## Red — proxy y DNS

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1048 | `Invoke-AtomicTest T1048` | ⬜ `soc_net_006_exfiltracion_volumen` | Registro del proxy |
| T1071.001 | `Invoke-AtomicTest T1071.001` | ⬜ `soc_net_001_beaconing` | Registro del proxy |
| T1071.004 | `Invoke-AtomicTest T1071.004` | ⬜ `soc_net_003_dns_tunel` | Suricata eve / DNS del resolutor |
| T1102 | `Invoke-AtomicTest T1102` | ⬜ `soc_net_002_c2_servicio_legitimo` | Registro del proxy |
| T1505.003 | `Invoke-AtomicTest T1505.003` | ⬜ `soc_net_005_webshell` | Acceso de nginx / apache |

## Aplicaciones web — registro del servidor web

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1059 | `Invoke-AtomicTest T1059` | ⬜ `web_008_inyeccion_jndi_log4shell` | Acceso de nginx / apache |
| T1059.004 | `Invoke-AtomicTest T1059.004` | ⬜ `web_007_inyeccion_de_comandos`<br>⬜ `web_012_shell_tras_explotacion` | Acceso de nginx / apache |
| T1059.007 | `Invoke-AtomicTest T1059.007` | ⬜ `web_002_xss_reflejado` | Acceso de nginx / apache |
| T1083 | `Invoke-AtomicTest T1083` | ⬜ `web_003_salto_de_directorio` | Acceso de nginx / apache |
| T1189 | `Invoke-AtomicTest T1189` | ⬜ `web_002_xss_reflejado` | Acceso de nginx / apache |
| T1190 | `Invoke-AtomicTest T1190` | ⬜ `web_001_inyeccion_sql`<br>⬜ `web_003_salto_de_directorio`<br>⬜ `web_004_ssrf_metadatos_nube`<br>⬜ `web_005_deserializacion_insegura`<br>⬜ `web_006_subida_fichero_ejecutable`<br>⬜ `web_007_inyeccion_de_comandos`<br>⬜ `web_008_inyeccion_jndi_log4shell`<br>⬜ `web_009_contrabando_peticiones`<br>⬜ `web_012_shell_tras_explotacion`<br>⬜ `web_013_inyeccion_plantillas_ssti` | Acceso de nginx / apache |
| T1505.003 | `Invoke-AtomicTest T1505.003` | ⬜ `web_006_subida_fichero_ejecutable`<br>⬜ `web_012_shell_tras_explotacion` | Acceso de nginx / apache |
| T1550.001 | `Invoke-AtomicTest T1550.001` | ⬜ `web_011_abuso_de_token_jwt` | Acceso de nginx / apache |
| T1552.005 | `Invoke-AtomicTest T1552.005` | ⬜ `web_004_ssrf_metadatos_nube` | Acceso de nginx / apache |
| T1595.002 | `Invoke-AtomicTest T1595.002` | ⬜ `web_010_escaneo_automatizado` | Acceso de nginx / apache |
| T1595.003 | `Invoke-AtomicTest T1595.003` | ⬜ `web_010_escaneo_automatizado` | Acceso de nginx / apache |
| T1606 | `Invoke-AtomicTest T1606` | ⬜ `web_011_abuso_de_token_jwt` | Acceso de nginx / apache |

## Exfiltración

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1005 | `Invoke-AtomicTest T1005` | ⬜ `exf_003_copia_masiva_extraible`<br>⬜ `exf_007_volcado_base_datos`<br>⬜ `exf_008_impresion_captura_masiva` | Sysmon EID 11 |
| T1020 | `Invoke-AtomicTest T1020` | ⬜ `exf_005_reenvio_correo_personal` | Registro de auditoria de M365 |
| T1048 | `Invoke-AtomicTest T1048` | ⬜ `exf_004_protocolo_alternativo` | Sysmon EID 1 |
| T1048.003 | `Invoke-AtomicTest T1048.003` | ⬜ `exf_004_protocolo_alternativo` | Sysmon EID 1 |
| T1052.001 | `Invoke-AtomicTest T1052.001` | ⬜ `exf_003_copia_masiva_extraible` | Sysmon EID 11 |
| T1074.001 | `Invoke-AtomicTest T1074.001` | ⬜ `exf_001_archivado_previo_exfiltracion`<br>⬜ `exf_007_volcado_base_datos` | Sysmon EID 1 |
| T1113 | `Invoke-AtomicTest T1113` | ⬜ `exf_008_impresion_captura_masiva` | Sysmon EID 1 |
| T1114.003 | `Invoke-AtomicTest T1114.003` | ⬜ `exf_005_reenvio_correo_personal` | Registro de auditoria de M365 |
| T1560.001 | `Invoke-AtomicTest T1560.001` | ⬜ `exf_001_archivado_previo_exfiltracion` | Sysmon EID 1 |
| T1567.001 | `Invoke-AtomicTest T1567.001` | ⬜ `exf_006_repositorio_publico_codigo` | Sysmon EID 1 |
| T1567.002 | `Invoke-AtomicTest T1567.002` | ⬜ `exf_002_subida_nube_personal` | Registro del proxy |

## XDR — manipulación de la telemetría

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1068 | `Invoke-AtomicTest T1068` | ⬜ `xdr_004_driver_vulnerable_byovd` | Canal Security / System de Windows |
| T1112 | `Invoke-AtomicTest T1112` | ⬜ `xdr_002_exclusiones_antivirus`<br>⬜ `xdr_003_reglas_asr_desactivadas`<br>⬜ `xdr_006_arranque_modo_seguro` | Sysmon EID 12/13/14 |
| T1489 | `Invoke-AtomicTest T1489` | ⬜ `xdr_001_desinstalacion_sensor_edr` | Sysmon EID 1 |
| T1562.001 | `Invoke-AtomicTest T1562.001` | ⬜ `xdr_001_desinstalacion_sensor_edr`<br>⬜ `xdr_002_exclusiones_antivirus`<br>⬜ `xdr_003_reglas_asr_desactivadas`<br>⬜ `xdr_004_driver_vulnerable_byovd` | Sysmon EID 1 |
| T1562.002 | `Invoke-AtomicTest T1562.002` | ⬜ `xdr_005_telemetria_etw_manipulada` | Sysmon EID 1 |
| T1562.006 | `Invoke-AtomicTest T1562.006` | ⬜ `xdr_005_telemetria_etw_manipulada` | Sysmon EID 1 |
| T1562.009 | `Invoke-AtomicTest T1562.009` | ⬜ `xdr_006_arranque_modo_seguro` | Sysmon EID 1 |

## Arquitectura Zero Trust

| Técnica ATT&CK | Atomic Red Team | Regla(s) Sigma (✅ detectada · ❌ no detectó · ⬜ sin probar) | Telemetría |
|---|---|---|---|
| T1021 | `Invoke-AtomicTest T1021` | ⬜ `zta_net_001_protocolo_en_claro` | network_connection |
| T1052.001 | `Invoke-AtomicTest T1052.001` | ⬜ `zta_dev_001_almacenamiento_extraible` | Canal Security / System de Windows |
| T1070.001 | `Invoke-AtomicTest T1070.001` | ⬜ `zta_vis_001_borrado_registro_auditoria` | Canal Security / System de Windows |
| T1078.002 | `Invoke-AtomicTest T1078.002` | ⬜ `zta_id_002_cuenta_servicio_interactiva` | Canal Security / System de Windows |
| T1078.004 | `Invoke-AtomicTest T1078.004` | ⬜ `zta_id_001_autenticacion_heredada` | Entra ID (SigninLogs / AuditLogs) |
| T1091 | `Invoke-AtomicTest T1091` | ⬜ `zta_dev_001_almacenamiento_extraible` | Canal Security / System de Windows |
| T1195.001 | `Invoke-AtomicTest T1195.001` | ⬜ `zta_sup_002_paquete_repositorio_no_aprobado`<br>⬜ `zta_sup_003_fichero_dependencias_modificado` | execve (auditd / Falco) |
| T1195.002 | `Invoke-AtomicTest T1195.002` | ⬜ `zta_sup_002_paquete_repositorio_no_aprobado` | execve (auditd / Falco) |
| T1556.006 | `Invoke-AtomicTest T1556.006` | ⬜ `zta_id_001_autenticacion_heredada` | Entra ID (SigninLogs / AuditLogs) |
| T1562.002 | `Invoke-AtomicTest T1562.002` | ⬜ `zta_vis_001_borrado_registro_auditoria` | Canal Security / System de Windows |
| T1574.001 | `Invoke-AtomicTest T1574.001` | ⬜ `zta_sup_001_libreria_ruta_no_estandar` | Sysmon EID 7 |
| T1574.002 | `Invoke-AtomicTest T1574.002` | ⬜ `zta_sup_001_libreria_ruta_no_estandar` | Sysmon EID 7 |

## Registro de resultados

Sale de `purple/resultados.csv` (columnas `fecha,tecnica,regla,detecto,siem,notas`).
Una fila por prueba ejecutada de verdad en el laboratorio. Es lo que convierte
la cobertura declarada en cobertura comprobada: una regla sin probar no es
cobertura, es una hipótesis.

| Fecha | Técnica | ¿Detectó? | Regla | SIEM | Notas |
|---|---|---|---|---|---|
| — | — | — | — | — | Todavía no hay ninguna ejecución registrada |

Tras cada ronda: añade las filas al CSV, ajusta las reglas que no saltaron
y vuelve a correr `python tools/build.py` para regenerar este mapa.

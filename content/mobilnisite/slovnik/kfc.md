---
slug: "kfc"
url: "/mobilnisite/slovnik/kfc/"
type: "slovnik"
title: "KFC – Key For Control Signalling"
date: 2026-01-01
abbr: "KFC"
fullName: "Key For Control Signalling"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/kfc/"
summary: "Kryptografický klíč speciálně odvozený pro ochranu zpráv signalizace řídicí roviny. Používá se k zajištění důvěrnosti a integrity kritických síťových řídicích příkazů a informací, a odděluje tak bezpe"
---

KFC je kryptografický klíč odvozený za účelem zajištění důvěrnosti a integrity zpráv signalizace řídicí roviny, což odděluje tuto bezpečnost od bezpečnosti roviny dat uživatele.

## Popis

Key For Control Signalling (KFC) je bezpečnostní klíč definovaný v konkrétních technických specifikacích 3GPP, zejména v těch, které se týkají zabezpečení pro Machine-Type Communications ([MTC](/mobilnisite/slovnik/mtc/)) a vylepšení pro CIoT (Cellular IoT). Jedná se o specializovaný klíč odvozený za účelem kryptografické ochrany signálních zpráv řídicí roviny vyměňovaných mezi uživatelským zařízením (UE), jako je například IoT zařízení, a sítí. Jeho hlavní rolí je zabezpečit řídicí rovinu, která přenáší příkazy, konfigurační aktualizace a správní informace, a to odděleně od uživatelské roviny, která přenázejí aplikační data.

Architektonicky je KFC součástí hierarchie klíčů. Typicky je odvozen z kořenového klíče vytvořeného během autentizace (např. K_[ASME](/mobilnisite/slovnik/asme/) v EPS nebo K_[AMF](/mobilnisite/slovnik/amf/) v 5GS) pomocí funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)). Do odvození se zahrnují specifické vstupní parametry, které klíč vážou k jeho účelu – signalizaci řídicí roviny – a příslušnému bezpečnostnímu kontextu. Tím je zajištěno kryptografické oddělení od klíčů používaných pro šifrování uživatelských dat (např. KUP) nebo pro jiné funkce řídicí roviny, jako je signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Klíč je uložen a používán v zabezpečeném prostředí na straně UE a příslušných síťových funkcí, jako je [MME](/mobilnisite/slovnik/mme/) v LTE nebo AMF v 5G.

Jak funguje, zahrnuje aplikaci klíče v rámci bezpečnostního protokolu. Po odvození se KFC používá jako vstupní klíč pro algoritmy ochrany integrity a šifrování aplikované na signální zprávy řídicí roviny. Například u určitých optimalizací CIoT, jako je optimalizace EPS pro CIoT v řídicí rovině, mohou být uživatelská data přenášena navázaná na signální zprávy NAS. V takových případech by se KFC použil k ochraně těchto zpráv NAS, které nyní nesou jak řídicí informace, tak uživatelská data. Konkrétní kryptografické algoritmy (např. 128-EEA1, 128-EIA1) a přesný bod aplikace (např. pro specifické protokolové datové jednotky) jsou definovány bezpečnostní politikou sítě a schopnostmi zařízení. Tím je zajištěno, že příkazy odeslané IoT zařízení (např. vzdářený restart, příkaz k aktualizaci firmwaru) nemohou být neoprávněnými stranami padělány, opakovány nebo odposlouchávány.

## K čemu slouží

KFC existuje proto, aby řešil odlišné bezpečnostní požadavky řídicí roviny, zejména v kontextu IoT a [MTC](/mobilnisite/slovnik/mtc/). Zařízení IoT často mají dlouhou životnost, jsou nasazována v nehlídaných nebo nepřátelských prostředích a komunikují sporadicky s malými datovými pakety. Bezpečnostní narušení v řídicí rovině by mohlo útočníkovi umožnit převzít kontrolu nad zařízeními, narušit služby nebo získat citlivé správní informace. Zavedením klíče určeného výhradně pro signalizaci řídicí roviny systém vynucuje bezpečnostní hranici; kompromitace klíče uživatelské datové relace automaticky neznamená kompromitaci klíčů chránících síťové příkazy.

Historicky poskytovaly starší mobilní systémy zabezpečení, ale často s méně podrobným oddělením klíčů přizpůsobeným pro objemnou lidskou komunikaci. Rozmach IoT si vyžádal optimalizace a vylepšené bezpečnostní modely pro zařízení s nízkou složitostí. Zavedení KFC, zejména kolem Release 14 s vylepšeními pro CIoT, bylo motivováno potřebou efektivního, a přesto robustního zabezpečení pro komunikaci IoT zaměřenou na řídicí rovinu. To zahrnuje scénáře, kdy jsou uživatelská data odesílána přes řídicí rovinu ke snížení signalizační režie, což činí ochranu tohoto kanálu řídicí roviny ještě kritičtější.

KFC navíc podporuje regulatorní a provozní požadavky na zabezpečenou správu zařízení. Pro utility, průmyslové senzory nebo monitorování infrastruktury je zásadní integrita příkazů jako 'uzavři ventil' nebo požadavků 'odečti měřič'. KFC poskytuje kryptografický základ pro zajištění autenticity a důvěrnosti těchto příkazů. Řeší tím problém poskytnutí cíleného a efektivního zabezpečení pro často kritický spoj pro řízení a kontrolu potenciálně obrovského množství omezených zařízení, bez režie neustálého znovunavazování plných bezpečnostních kontextů pro přenosy malých dat.

## Klíčové vlastnosti

- Specializovaný klíč pro ochranu důvěrnosti a integrity signalizace řídicí roviny
- Odvozen z kořenového klíče pomocí KDF s parametry specifickými pro daný účel
- Poskytuje kryptografické oddělení od klíčů pro provoz v uživatelské rovině (KUP)
- Kritický pro zabezpečení správy IoT zařízení a řídicích zpráv
- Používá se v optimalizacích CIoT EPS pro ochranu zpráv NAS přenášejících uživatelská data
- Umožňuje zabezpečenou konfiguraci a řízení zařízení 'over-the-air'

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services

---

📖 **Anglický originál a plná specifikace:** [KFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/kfc/)

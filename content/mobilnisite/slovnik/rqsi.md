---
slug: "rqsi"
url: "/mobilnisite/slovnik/rqsi/"
type: "slovnik"
title: "RQSI – Reflective QoS Indication"
date: 2025-01-01
abbr: "RQSI"
fullName: "Reflective QoS Indication"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rqsi/"
summary: "Zastaralá indikace QoS používaná v před-5G systémech 3GPP, konkrétně pro služby založené na IMS. Jednalo se o parametr v signalizaci SIP/SDP, který indikoval, že mediální tok má používat síťově inicio"
---

RQSI je zastaralý signalizační parametr SIP/SDP v systémech před 5G, který indikuje, že pro mediální tok by měla být použita síťově iniciovaná QoS (např. PCC) pro služby IMS.

## Popis

Reflective QoS Indication (RQSI) je parametr definovaný v dřívějších vydáních 3GPP, primárně v kontextu IP Multimedia Subsystem (IMS) a Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) pro sítě 3G a 4G. Na rozdíl od 5G [RQI](/mobilnisite/slovnik/rqi/), což je značka v uživatelské rovině, je RQSI indikátor na aplikační vrstvě vyměňovaný v rámci zpráv Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) během navazování IMS relace (např. nastavení VoIP hovoru). Jeho účelem je signalizovat z IMS Application Server ([AS](/mobilnisite/slovnik/as/)) nebo z UE do architektury PCC, že požadovaný mediální tok vyžaduje síťově iniciovanou alokaci QoS prostředků.

Architektonicky RQSI funguje ve služební vrstvě. Když IMS koncový bod (UE nebo síťový server) zahrne do nabídky nebo odpovědi SDP pro mediální proud (audio, video) atribut 'gpp:rqsi' na úrovni média, tento atribut funguje jako žádost nebo instrukce pro podpůrnou přenosovou síť. [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function), která funguje jako vstupní bod IMS, tuto signalizaci SIP/SDP zachytí. Po detekci parametru RQSI P-CSCF informuje Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/) v 4G) přes rozhraní Rx. PCRF pak použije toto jako spouštěč pro generování příslušných pravidel PCC, která jsou předána Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a nakonec vedou k vytvoření vyhrazeného přenosového kanálu se specifickou QoS (např. přenosový kanál se zaručenou přenosovou rychlostí) pro daný mediální tok.

Jak to funguje, zahrnuje interakci mezi vrstvami. Aplikace (IMS) vyjádří svou potřebu QoS pomocí RQSI v SDP. P-CSCF provede autorizaci na služební úrovni a přeloží tento aplikační požadavek do žádosti o síťové prostředky přes rozhraní Rx. PCRF jako centrální bod pro rozhodování o politikách vytvoří PCC pravidlo, které mapuje popis média v SDP (IP adresy, porty) na specifický identifikátor třídy QoS (QCI) a případně přenosové rychlosti. Toto pravidlo je pak vynuceno PGW a rádiovou přístupovou sítí, což zajišťuje, že mediální tok obdrží smluvenou QoS. Samotný RQSI není viditelný v uživatelské rovině; je to čistě spouštěč ze služební do řídicí roviny.

Jeho role v zastaralých sítích spočívala v umožnění IMS aplikacím dynamicky žádat o garantovanou QoS z paketové domény, což byl klíčový požadavek pro hlas a video přes LTE (VoLTE). Poskytoval standardizovaný mechanismus, kterým mohla vrstva IMS komunikovat své potřeby do rámce PCC, čímž překlenula mezeru mezi aplikační signalizací a správou přenosových kanálů. To bylo nezbytné pro dosažení konzistentní kvality v plně IP komunikačních službách.

## K čemu slouží

RQSI bylo vytvořeno, aby řešilo klíčovou výzvu v raných nasazeních LTE/EPC: umožnit službám reálné komunikace založeným na IMS, jako je VoLTE, spolehlivě žádat a přijímat odpovídající síťové prostředky. V počátečních sítích pouze pro data používal veškerý provoz výchozí přenosové kanály s best-effort QoS, což bylo nevhodné pro zpoždění citlivý hlas. Nebyl žádný standardní způsob, jak by IMS aplikace mohla explicitně požádat EPC o vyhrazený přenosový kanál s garantovanou QoS.

Problém, který řešilo, byl nedostatek provázání mezi signalizací aplikační relace (SIP) a nastavením síťových prostředků. Bez RQSI se síťově iniciovaná QoS pro IMS spoléhala na statickou konfiguraci nebo nestandardní metody, což vedlo k problémům s interoperabilitou a špatným uživatelským zážitkem. Parametr RQSI, zavedený přibližně ve 3GPP Release 11, poskytl standardizovaný 'háček' uvnitř SDP, který mohl P-CSCF rozpoznat a podle něj jednat, čímž spouštěl dynamické PCC procedury.

Historicky představuje vývoj směrem k aplikacím vědomému síťování v mobilních systémech. Podnítilo těsnější integraci mezi služební vrstvou (IMS) a vrstvou řízení politik (PCC). Zatímco jeho funkční cíl – spuštění síťové QoS pro aplikační tok – je podobný 5G RQI, mechanismy jsou značně odlišné: RQSI používá signalizaci na aplikační vrstvě (SIP) ke spuštění akcí v řídicí rovině jádra sítě (PCRF), zatímco 5G RQI používá značkování v uživatelské rovině ke spuštění akcí lokálních v UE. RQSI je tedy předchůdcem konceptu, který zdůraznil potřebu dynamické QoS, ale spoléhal na centralizovanější, signalizací zatíženou architekturu.

## Klíčové vlastnosti

- Atribut na úrovni média v SDP ('gpp:rqsi') používaný v signalizaci IMS.
- Signalizuje žádost o síťově iniciovanou QoS pro konkrétní mediální tok.
- Zachytává se P-CSCF během navazování SIP relace.
- Spouští rozhodnutí o politice v PCRF a nastavení vyhrazeného přenosového kanálu přes PCC.
- Používá se primárně pro zajištění služeb VoLTE a ViLTE.
- Funguje na rozhraní mezi aplikací a řídicí rovinou.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)

## Definující specifikace

- **TS 24.139** (Rel-19) — UE-EPC Procedures for Fixed Broadband Access
- **TS 24.820** (Rel-11) — 3GPP-Fixed Broadband Interworking Procedures

---

📖 **Anglický originál a plná specifikace:** [RQSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rqsi/)

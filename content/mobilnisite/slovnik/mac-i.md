---
slug: "mac-i"
url: "/mobilnisite/slovnik/mac-i/"
type: "slovnik"
title: "MAC-I – Message Authentication Code for Integrity"
date: 2025-01-01
abbr: "MAC-I"
fullName: "Message Authentication Code for Integrity"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mac-i/"
summary: "Kód pro ověření zpráv (Message Authentication Code - MAC) používaný k zajištění ochrany integrity a autentizace původu dat pro signalizační zprávy a v některých případech i pro uživatelská data v sítí"
---

MAC-I je kód pro ověření zpráv (Message Authentication Code) používaný v sítích 3GPP k zajištění ochrany integrity a autentizace původu dat pro signalizační zprávy a některá uživatelská data, což zaručuje, že nebyly pozměněny a pocházejí z autorizovaného zdroje.

## Popis

MAC-I (Message Authentication Code for Integrity) je kryptografický kontrolní součet připojený k protokolovým datovým jednotkám (PDU) v protokolech rádiového přístupu a jádra sítě 3GPP, který zaručuje jejich integritu. Na rozdíl od [MAC-A](/mobilnisite/slovnik/mac-a/), který se používá pro počáteční autentizaci, se MAC-I používá pro průběžnou ochranu integrity signalizačních zpráv po navázání bezpečnostních kontextů. Je generován pomocí vyhrazeného integritního klíče ([IK](/mobilnisite/slovnik/ik/)), parametru čerstvosti (COUNT), směrového bitu, samotné zprávy a identifikátoru přenosového kanálu. Nejčastěji odkazované algoritmy pro jeho výpočet jsou sady 128-EEA/128-EIA definované pro LTE a NR, jako jsou SNOW 3G, [AES](/mobilnisite/slovnik/aes/) a ZUC.

V protokolovém zásobníku je MAC-I primárně spojován se signalizačními vrstvami Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)). Například v LTE (TS 36.323) je vrstva PDCP (Packet Data Convergence Protocol) odpovědná za ochranu integrity a verifikaci RRC zpráv pomocí MAC-I. Vysílající entita (UE nebo eNodeB) vypočte MAC-I nad RRC PDU a zahrne jej do paketu. Přijímající entita nezávisle přepočítá MAC-I pomocí stejných vstupů a klíčů. Pokud se vypočtená hodnota shoduje s přijatým MAC-I, je zpráva považována za neporušenou a autentickou. Neshoda spustí bezpečnostní selhání, které typicky vede k uvolnění rádiového spojení.

Proces zahrnuje stavový čítač (COUNT) pro prevenci opakovaných útoků (replay attacks), což zajišťuje, že i identické zprávy odeslané v různých časech dají různé hodnoty MAC-I. Směrový bit rozlišuje mezi uplink a downlink provozem, čímž zabraňuje útokům typu reflection. Z architektonického hlediska je integritní klíč (IK) používaný pro MAC-I odvozen během procedury [AKA](/mobilnisite/slovnik/aka/) z kořenového klíče K. V EPS je IK součástí odvození Kasme; v 5GS je odvozen z KAMF. Tím vzniká kryptograficky oddělená hierarchie klíčů, kde kompromitace přenosových klíčů neovlivní autentizační klíče.

Role MAC-I přesahuje RRC. V jádru sítě se mechanismus MAC-I používá také pro ochranu integrity NAS zpráv mezi UE a [MME](/mobilnisite/slovnik/mme/) (v EPS) nebo [AMF](/mobilnisite/slovnik/amf/) (v 5GS), i když konkrétní algoritmus a klíč se mohou lišit (používá se KNASint). Jedná se o povinnou bezpečnostní funkci pro veškerou signalizaci řídicí roviny v moderních sítích 3GPP, která tvoří zásadní obranu proti manipulaci, vkládání zpráv a opakovaným útokům na rozhraní vzduchu a uvnitř hranic důvěry sítě.

## K čemu slouží

MAC-I byl zaveden, aby řešil kritickou potřebu integrity a autentizace původu řídicí signalizace v paketově přepínaných mobilních sítích. Starší systémy s přepojováním okruhů, jako je GSM, poskytovaly omezenou ochranu signalizace, zaměřenou primárně na šifrování rádiového rozhraní, což činilo řídicí kanály zranitelnými vůči manipulaci. Jak se sítě vyvíjely směrem k architekturám plně založeným na IP s LTE a 5G, riziko, že útočníci změní nebo zfalšují signalizační zprávy (např. příkazy k předání spojení, žádosti o zřízení přenosového kanálu nebo pagingové zprávy) za účelem narušení služby, způsobení odmítnutí služby (DoS) nebo přesměrování provozu, se stalo prvořadým problémem.

Jeho vytvoření bylo motivováno požadavkem na robustní, standardizovaný mechanismus ochrany integrity, který by mohl být aplikován skokově (např. přes rozhraní Uu na vzduchu) a koncově (např. pro NAS). Problém, který řeší, je zajištění, že kritické síťové řídicí příkazy nelze bez odhalení pozměnit. Bez MAC-I by útočník mohl změnit příkaz k předání spojení a přinutit UE k připojení ke škodlivé buňce nebo upravit pagingovou zprávu ke sledování polohy uživatele.

MAC-I navíc umožňuje bezpečné navázání dalších bezpečnostních kontextů. Například signalizace RRC chráněná integritou se používá k bezpečnému přenosu konfigurace šifrovacího algoritmu a zašifrovaného příkazu režimu zabezpečení uživatelské roviny. Tvoří nezbytnou vrstvu v strategii obrany do hloubky pro sítě 3GPP, která spolupracuje se šifrováním pro důvěrnost (pomocí ENC algoritmů) a AKA pro počáteční autentizaci. Jeho stavový návrh s čítači také řeší omezení statických kódů pro ověření zpráv tím, že poskytuje ochranu proti opakování, což je klíčová vlastnost pro časově citlivé mobilní procedury.

## Klíčové vlastnosti

- Poskytuje ochranu integrity a autentizaci původu dat pro signalizační zprávy RRC a NAS.
- Používá vyhrazený integritní klíč (IK) odvozený z kořenového klíče během AKA.
- Zahrnuje čítač (COUNT) a směrový bit pro prevenci opakovaných útoků (replay attacks) a útoků typu reflection.
- Vypočítává se a ověřuje na vrstvě PDCP (pro RRC) a na vrstvě NAS v protokolovém zásobníku.
- Povinný pro zabezpečení řídicí roviny v LTE a NR; selhání vede k uvolnění spojení.
- Podporuje více možností kryptografických algoritmů (např. SNOW 3G, AES, ZUC) podle 128-EIA.

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 38.323** (Rel-19) — Packet Data Convergence Protocol (PDCP)

---

📖 **Anglický originál a plná specifikace:** [MAC-I na 3GPP Explorer](https://3gpp-explorer.com/glossary/mac-i/)

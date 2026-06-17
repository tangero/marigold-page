---
slug: "3gms"
url: "/mobilnisite/slovnik/3gms/"
type: "slovnik"
title: "3GMS – Third Generation Mobile Communications System"
date: 2025-01-01
abbr: "3GMS"
fullName: "Third Generation Mobile Communications System"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/3gms/"
summary: "3GMS označuje komplexní bezpečnostní architekturu a mechanismy definované pro sítě 3G (UMTS). Poskytuje rámec pro autentizaci, utajení a ochranu integrity a vytváří tak základ pro zabezpečenou mobilní"
---

3GMS je komplexní bezpečnostní architektura pro sítě 3G (UMTS), která poskytuje rámec pro autentizaci, utajení a ochranu integrity za účelem navázání zabezpečené mobilní komunikace.

## Popis

Bezpečnostní architektura Third Generation Mobile Communications System (3GMS) je komplexní rámec definovaný ve specifikacích 3GPP, především v TS 33.106 a TS 33.107. Byla navržena tak, aby řešila bezpečnostní nedostatky systémů 2G (GSM) a poskytla robustní bezpečnostní základ pro sítě Universal Mobile Telecommunications System (UMTS). Architektura je postavena na souboru bezpečnostních funkcí a mechanismů, které chrání síť, uživatele a poskytované služby.

Jádrem bezpečnosti 3GMS je protokol Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Na rozdíl od jednosměrné autentizace v GSM (síť autentizuje uživatele) poskytuje UMTS AKA vzájemnou autentizaci mezi uživatelským zařízením (UE) a sítí. Protokol je založen na mechanismu výzva-odpověď s využitím předem sdíleného tajného klíče (K) uloženého na USIM a v Authentication Centre (AuC) v rámci domovského prostředí ([HE](/mobilnisite/slovnik/he/)). Obsluhující síť žádá o autentizační vektory (kvintice) z HE, které se skládají z náhodné výzvy (RAND), očekávané odpovědi (XRES), šifrovacího klíče ([CK](/mobilnisite/slovnik/ck/)), integritního klíče ([IK](/mobilnisite/slovnik/ik/)) a autentizačního tokenu ([AUTN](/mobilnisite/slovnik/autn/)). UE použije AUTN k autentizaci sítě a RAND k výpočtu své odpovědi (RES), která je odeslána zpět k ověření.

Mezi klíčové bezpečnostní služby poskytované 3GMS patří utajení identity uživatele, autentizace entit, utajení dat a integrita dat. Utajení identity uživatele je dosaženo použitím dočasné identity (TMSI) na rádiovém rozhraní namísto trvalého International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). Utajení dat (šifrování) se aplikuje na uživatelská data a některé signalizační zprávy na rádiovém přístupovém spoji (mezi UE a RNC) pomocí šifrovacího klíče (CK) a algoritmu UEA (UMTS Encryption Algorithm). Ochrana integrity dat, což je nová funkce oproti GSM, se aplikuje na kritické signalizační zprávy pomocí integritního klíče (IK) a algoritmu UIA (UMTS Integrity Algorithm), čímž se zabrání modifikaci zpráv a útokům opakováním.

Architektura definuje pět skupin bezpečnostních funkcí: Network Access Security (I), Network Domain Security ([II](/mobilnisite/slovnik/ii/)), User Domain Security ([III](/mobilnisite/slovnik/iii/)), Application Domain Security (IV) a Visibility and Configurability of Security (V). Skupina I, nejkritičtější, pokrývá bezpečnostní mechanismy pro rádiový přístupový spoj, včetně AKA, šifrování a integrity. Skupina II zabezpečuje signalizační a uživatelské datové výměny mezi síťovými uzly (např. mezi RNC a core network) pomocí protokolů jako MAPSec a IPSec. Tento vrstvený přístup zajišťuje principy zabezpečení end-to-end napříč různými doménami sítě 3G.

## K čemu slouží

Bezpečnost 3GMS byla vytvořena, aby řešila dobře zdokumentované bezpečnostní slabiny jejího předchůdce, systému 2G GSM. GSM mělo několik kritických zranitelností: poskytovalo pouze jednosměrnou autentizaci (síť autentizuje uživatele), což jej činilo zranitelným vůči útokům falešných základnových stanic; šifrovací algoritmy (A5/1, A5/2) byly nakonec shledány slabými; a chyběla ochrana integrity signalizace, což ji činilo náchylnou k manipulaci. Primární motivací pro 3GMS bylo navrhnout bezpečnostní architekturu od základů, která by byla robustní vůči známým a předvídatelným útokům, a umožnit tak zabezpečené mobilní datové služby a budovat důvěru uživatelů pro nové aplikace, jako je mobilní obchod.

Historickým kontextem byl přechod od primárně hlasově orientovaných sítí 2G k sítím 3G navrženým pro multimédia, přístup k internetu a bohatší datové služby. Tyto nové služby nesly vyšší hodnotu a větší obavy o soukromí, což vyžadovalo silnější zabezpečení. Dále regulační a komerční prostředí požadovalo lepší ochranu uživatelských dat a identity. 3GMS si kladla za cíl poskytnout budoucím potřebám vyhovující základ, s funkcemi jako agilita algoritmů (schopnost zavádět nové kryptografické algoritmy) a zvýšené délky klíčů, aby odolaly rostoucí výpočetní síle dostupné útočníkům.

Vyřešila problém nezabezpečených rádiových spojů a nedůvěryhodných obsluhujících sítí zavedením vzájemné autentizace, čímž zajistila, že uživatel může ověřit, že se připojuje k legitimní síti. Také oddělila šifrovací a integritní klíče, což umožnilo nezávislé řízení síly a životního cyklu těchto dvou funkcí. Definováním jasné bezpečnostní architektury napříč více doménami poskytla síťovým operátorům a výrobcům zařízení standardizovaný plán pro implementaci interoperabilního a vysoce důvěryhodného zabezpečení, což bylo klíčové pro globální nasazení UMTS.

## Klíčové vlastnosti

- Vzájemná autentizace prostřednictvím protokolu UMTS AKA
- Utajení dat (šifrování) pro uživatelská a signalizační data na rozhraní Uu
- Ochrana integrity dat pro signalizační zprávy
- Utajení identity uživatele pomocí dočasných identit (TMSI)
- Agilita algoritmů pro šifrování (UEA) a integritu (UIA)
- Oddělení šifrovacího klíče (CK) a integritního klíče (IK)

## Definující specifikace

- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [3GMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/3gms/)

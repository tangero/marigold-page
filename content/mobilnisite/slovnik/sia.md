---
slug: "sia"
url: "/mobilnisite/slovnik/sia/"
type: "slovnik"
title: "SIA – SS7 security gateway Integrity Algorithm identifier"
date: 2025-01-01
abbr: "SIA"
fullName: "SS7 security gateway Integrity Algorithm identifier"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sia/"
summary: "Identifikátor používaný v protokolech bezpečnostní brány SS7 k určení kryptografického algoritmu integrity aplikovaného na signalizační zprávy. Je součástí bezpečnostního mechanismu pro ochranu starší"
---

SIA je identifikátor používaný v protokolech bezpečnostní brány SS7 k určení kryptografického algoritmu integrity aplikovaného na signalizační zprávy za účelem ochrany proti odposlechu a neoprávněným zásahům.

## Popis

SIA ([SS7](/mobilnisite/slovnik/ss7/) security gateway Integrity Algorithm identifier) je specifický parametr používaný v bezpečnostním kontextu bran Signalizačního systému č. 7 (SS7), zejména těch, které implementují funkci Bezpečnostní brány ([SEG](/mobilnisite/slovnik/seg/)) specifikovanou 3GPP v TS 33.204. Funguje v rámci architektury Network Domain Security ([NDS](/mobilnisite/slovnik/nds/)) pro protokoly založené na IP ([NDS/IP](/mobilnisite/slovnik/nds-ip/)), která byla rozšířena pro ochranu signalizace SS7. Identifikátor SIA je přenášen v rámci výměn bezpečnostních protokolů, jako je protokol Internet Key Exchange ([IKE](/mobilnisite/slovnik/ike/)) používaný k navázání [IPsec](/mobilnisite/slovnik/ipsec/) Security Associations ([SA](/mobilnisite/slovnik/sa/)), aby vyjednal a dohodl konkrétní kryptografický algoritmus, který bude použit k zajištění integrity signalizačních zpráv SS7 přenášených přes IP síť.

Architektonicky se SIA používá ve scénářích, kdy je starší signalizace SS7 (např. [MAP](/mobilnisite/slovnik/map/), CAP) přenášena přes IP sítě, jako jsou sítě GRX/IPX používané pro mezinárodní roaming. Bezpečnostní brána (SEG) se nachází na hranici sítě operátora a zabezpečuje veškerý provoz NDS/IP do jiných sítí a z nich. Když dvě SEG navazují zabezpečený tunel, musí vyjednat bezpečnostní sadu, která zahrnuje šifrovací algoritmy, algoritmy integrity a související parametry. SIA je identifikátor, který odkazuje na dohodnutý algoritmus integrity (např. HMAC-SHA-1-96, AES-XCBC-MAC-96) pro ochranu přenášených signalizačních dat SS7.

Jeho fungování je integrováno do procesu vyjednávání IKEv1 nebo IKEv2. Během fáze protokolu Internet Security Association and Key Management Protocol (ISAKMP) si SEG vyměňují seznamy podporovaných bezpečnostních návrhů. Každý návrh obsahuje identifikátory pro algoritmus integrity (SIA), šifrovací algoritmus a další atributy. Hodnota SIA je číselný nebo textový identifikátor definovaný v registrech IANA nebo specifikacích 3GPP. Protistrany vyberou vzájemně podporovaný algoritmus a jeho identifikátor (SIA) je následně použit pro konfiguraci IPsec SA. Následně bude integrita všech zpráv SS7 chráněných touto SA ověřována pomocí algoritmu odpovídajícího vyjednanému SIA, typicky přidáním Integrity Check Value (ICV) ke každému paketu.

Jeho role je klíčová pro udržení důvěryhodnosti a bezpečnosti signalizace mezi operátory, která je páteří služeb mobility a roamingu. Tím, že explicitně identifikuje algoritmus integrity, SIA zajišťuje, že oba koncové body zabezpečeného tunelu aplikují stejné kryptografické výpočty pro ověření, že signalizační zprávy nebyly během přenosu pozměněny. Tím chrání proti útokům vkládání, mazání a modifikace zpráv, které by mohly vést k podvodům (např. neoprávněné sledování polohy, odposlech hovorů) nebo narušení služeb. SIA spolu se svým protějškem pro šifrování (identifikátor šifrovacího algoritmu) tvoří jádro kryptografické politiky pro spoje SS7-over-IP v rámci architektury 3GPP NDS/IP.

## K čemu slouží

Identifikátor SIA byl vytvořen jako součást práce 3GPP na Network Domain Security (NDS), zahájené kolem Release 8, aby řešil závažné bezpečnostní zranitelnosti odhalené, když se tradiční přepojovaná signalizace SS7 začala přenášet přes IP sítě. Starší síť SS7 byla navržena pro uzavřené, důvěryhodné skupiny operátorů a měla minimální inherentní zabezpečení. Když operátoři přecházeli na IP páteřní sítě (jako GRX) kvůli nákladům a efektivitě, signalizace se stala zranitelnou vůči útokům založeným na IP, jako je odposlech, falšování identity a manipulace se zprávami. Účelem SIA a širšího NDS/IP pro SS7 bylo poskytnout standardizovanou, interoperabilní metodu pro kryptografickou ochranu těchto kritických signalizačních spojů.

Řeší problém nejednoznačnosti vyjednávání algoritmů v prostředí s více dodavateli a více operátory. Různí dodavatelé síťového vybavení mohou podporovat různé sady kryptografických algoritmů. Bez standardizovaného způsobu identifikace a výběru algoritmu integrity během nastavování bezpečnostní asociace by interoperabilita selhala nebo by mohly být tiše vybrány slabší algoritmy. SIA poskytuje jasný, dohodnutý identifikátor, kterému rozumějí všechny kompatibilní SEG, a zajišťuje, že je konzistentně aplikován silný, vzájemně přijatelný algoritmus ochrany integrity. To byla klíčová omezení dřívějších ad-hoc bezpečnostních implementací pro SS7 přes IP.

Historický kontext je vývoj zabezpečení core sítě. Před NDS bylo zabezpečení často implementováno na síťové perimetrii pomocí firewallů, které nechránily samotné signalizační zprávy. Motivací pro vytvoření SIA bylo bezproblémově integrovat zabezpečení SS7 do dobře zavedené architektury IPsec používané pro obecné zabezpečení IP. Definováním specifických identifikátorů, jako je SIA, pro použití v rámci vyjednávání IKE/IPsec pro provoz SS7, umožnilo 3GPP operátorům využívat robustní kryptografii založenou na standardech k ochraně své roamingové a propojovací signalizace, čímž zmírnilo rizika podvodů a zajistilo dostupnost služeb, jak se sítě vyvíjely směrem k plně IP architekturám.

## Klíčové vlastnosti

- Standardizovaný identifikátor pro algoritmy integrity v protokolech bezpečnostní brány SS7.
- Používá se během vyjednávání IKE/IPsec Security Association mezi Bezpečnostními branami (SEG).
- Součást architektury 3GPP Network Domain Security for IP (NDS/IP) definované v TS 33.204.
- Zajišťuje interoperabilitu tím, že umožňuje protistranám dohodnout se na vzájemně podporovaném kryptografickém algoritmu.
- Chrání integritu starších signalizačních zpráv SS7 (MAP, CAP) přenášených přes IP sítě.
- Funguje ve spojení s identifikátory šifrovacích algoritmů k definování kompletní bezpečnostní sady.

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [IKE – Internet Key Exchange](/mobilnisite/slovnik/ike/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sia/)

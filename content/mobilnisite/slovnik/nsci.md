---
slug: "nsci"
url: "/mobilnisite/slovnik/nsci/"
type: "slovnik"
title: "NSCI – New Security Context Indicator"
date: 2025-01-01
abbr: "NSCI"
fullName: "New Security Context Indicator"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nsci/"
summary: "Příznak používaný v signalizaci NGAP (Next Generation Application Protocol) k označení, že byl pro UE vytvořen nový bezpečnostní kontext. Spouští v uzlu RAN aplikaci nových kryptografických klíčů, čím"
---

NSCI je příznak v signalizaci NGAP, který indikuje, že byl zaveden nový bezpečnostní kontext, a spouští v RAN aplikaci nových kryptografických klíčů pro ochranu proti replay útokům.

## Popis

New Security Context Indicator (NSCI) je kritický bezpečnostní parametr v rámci protokolu [NG](/mobilnisite/slovnik/ng/) Application Protocol ([NGAP](/mobilnisite/slovnik/ngap/)) podle 3GPP, což je signalizační protokol mezi funkcí [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) 5G jádra a uzlem NG-RAN (gNB). Jedná se o jednoduchý booleovský indikátor (jeden bit) obsažený v konkrétních zprávách NGAP, především v INITIAL CONTEXT SETUP REQUEST a PATH SWITCH REQUEST ACKNOWLEDGE. Jeho hlavní funkcí je signalizovat gNB, že jádrová síť pro dané uživatelské zařízení (UE) vytvořila zcela nový bezpečnostní kontext. 'Nový bezpečnostní kontext' znamená, že jádrová síť (AMF a Authentication Server Function, [AUSF](/mobilnisite/slovnik/ausf/)) provedla s UE nové primární ověření a proceduru dohody o klíči, což vedlo ke generování nové sady kryptografických klíčů odlišné od všech dříve použitých klíčů.

Při přijetí zprávy NGAP s nastaveným NSCI na 'true' gNB chápe, že musí pro dané UE odvodit a použít novou sadu bezpečnostních klíčů přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)). Tyto AS klíče, konkrétně KgNB (základní klíč pro gNB) a následně odvozené klíče pro ochranu integrity (KRRCint) a důvěrnosti (KRRCenc, KUPenc), jsou vypočteny pomocí nového kotvícího klíče z jádrové sítě (KAUSF nebo odvozeného KAMF) a nových náhodných hodnot. Tento proces je klíčový, protože zajišťuje kryptografické oddělení mezi různými bezpečnostními relacemi. Pokud je NSCI nastaveno na 'false', může gNB odvodit nové klíče na základě stávajícího klíčového kontextu, typicky pomocí funkce odvození klíče s novými vstupními parametry (jako je parametr Next Hop, [NH](/mobilnisite/slovnik/nh/)), což je běžné během předání spojení v rámci stejné AMF.

Role NSCI je zásadní pro zmírnění bezpečnostních hrozeb, zejména replay útoků. Během předání spojení mezi různými AMF nebo po proceduře service request po režimu nečinnosti, pokud se jádrová síť rozhodne, že je nutné úplné přerovnání (např. z důvodu bezpečnostní politiky, vypršení časovače nebo podezření z kompromitace), vytvoří nový bezpečnostní kontext. Jeho explicitní indikace RAN prostřednictvím NSCI zaručuje, že starý kryptografický materiál nemůže být znovu použit, ani kdyby útočník zachytil předchozí signalizační zprávy. Tento mechanismus je klíčovou součástí forward security v 5G, která zajišťuje, že kompromitace klíče jedné relace neovlivní bezpečnost relací budoucích. Zpracování NSCI gNB je povinné a těsně integrované s bezpečnostní architekturou 5G definovanou v TS 33.501.

## K čemu slouží

NSCI bylo zavedeno v 5G (Release 15), aby poskytlo explicitní a spolehlivý signalizační mechanismus pro čerstvost bezpečnostního kontextu a řešilo tak omezení a nejednoznačnosti přítomné v předchozích generacích, jako je LTE. V LTE byla indikace nového bezpečnostního kontextu implicitní nebo vázaná na konkrétní procedury, což mohlo vést k implementačním nejasnostem a potenciálním bezpečnostním zranitelnostem. Například v určitých scénářích předání spojení nemuselo být pro [eNB](/mobilnisite/slovnik/enb/) zcela jednoznačné, zda má použít čerstvě odvozený klíč, nebo klíč odvozený z předchozího materiálu. Tuto nejednoznačnost by bylo možné zneužít ve složitých útocích.

Základní problém, který NSCI řeší, je zajištění synchronizovaného bezpečnostního stavu mezi jádrovou sítí a RAN. Jádrová síť ([AMF](/mobilnisite/slovnik/amf/)/AUSF) je nejvyšší autoritou pro ověření UE a generování klíčů. Když se rozhodne obnovit bezpečnostní kontext, musí být RAN jednoznačně informována, aby zahodila veškerý starý klíčový materiál a začala používat nové klíče. NSCI poskytuje tento jasný, v pásmu přenášený signál v rámci standardní signalizace NGAP. To je obzvláště důležité pro vylepšené scénáře mobility v 5G, včetně předání spojení mezi systémy a připojení k nepřístupům 3GPP, kde může být nutné bezpečnostní kontext obnovovat častěji. Jeho vytvoření bylo motivováno potřebou silnější, explicitnější a budoucí vývoj zohledňující bezpečnostní signalizace pro podporu rozmanitých a náročných případů užití 5G, včetně massive IoT a ultra-spolehlivé komunikace, kde je robustnost zabezpečení prvořadá.

## Klíčové vlastnosti

- Booleovský indikátor v kritických zprávách NGAP (např. INITIAL CONTEXT SETUP REQUEST).
- Explicitně signalizuje vytvoření zcela nového bezpečnostního kontextu z jádrové sítě do RAN.
- Spouští odvození a aplikaci nové sady kryptografických klíčů přístupové vrstvy (AS) (KgNB) v gNB.
- Nezbytné pro vynucení bezpečnostních politik vyžadujících periodické přerovnání.
- Zmírňuje replay útoky tím, že zajišťuje neopakované použití starých klíčů po obnovení bezpečnostního kontextu.
- Podporuje robustní zabezpečení během předání spojení mezi různými AMF a procedur service request po režimu nečinnosti.

## Definující specifikace

- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [NSCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsci/)

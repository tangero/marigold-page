---
slug: "cts-pin"
url: "/mobilnisite/slovnik/cts-pin/"
type: "slovnik"
title: "CTS-PIN – CTS-Personal Identification Number"
date: 2025-01-01
abbr: "CTS-PIN"
fullName: "CTS-Personal Identification Number"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cts-pin/"
summary: "Bezpečnostní přihlašovací údaj používaný v mechanismu Circuit Switched FallBack (CSFB) pro ověření a autorizaci uživatele, když zařízení přechází (fallback) na okruhově přepínanou síť 2G/3G. Zajišťuje"
---

CTS-PIN je bezpečnostní přihlašovací údaj používaný v mechanismu Circuit Switched FallBack (CSFB) k ověření a autorizaci zařízení uživatele pro zabezpečený přístup k zastaralým okruhově přepínaným hlasovým sítím.

## Popis

CTS-Personal Identification Number (CTS-PIN) je bezpečnostní funkce definovaná ve specifikacích 3GPP, která umožňuje zabezpečené ověření uživatele během procedur Circuit Switched FallBack ([CSFB](/mobilnisite/slovnik/csfb/)). CSFB je mechanismus, který umožňuje uživatelskému zařízení (UE) připojenému k 4G LTE síti, která je pro hovory čistě paketově přepínaná, přejít (fallback) na zastaralou okruhově přepínanou síť 2G (GSM) nebo 3G (UMTS) k uskutečnění hlasového hovoru. CTS-PIN je klíčovou součástí tohoto předání, funguje jako sdílené tajemství mezi UE a sítí k ověření identity uživatele a autorizaci přístupu k okruhově přepínané doméně.

Architektonicky je CTS-PIN uložen na dvou klíčových místech: v modulu Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) v zařízení uživatele a v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v jádru sítě. Když je spuštěna procedura CSFB, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) obsluhující cílovou síť 2G/3G požaduje od HLR/HSS autentizační vektory. Tyto vektory jsou odvozeny s využitím CTS-PIN jako jednoho ze vstupů spolu s dalšími parametry, jako je náhodná výzva ([RAND](/mobilnisite/slovnik/rand/)). MSC odešle RAND k UE, které použije svůj lokálně uložený CTS-PIN a stejný kryptografický algoritmus k výpočtu odpovědi ([SRES](/mobilnisite/slovnik/sres/)). Síť porovná přijatý SRES s vlastní vypočítanou hodnotou; shoda ověří uživatele a umožní pokračování okruhově přepínaného hovoru.

Role CTS-PIN spočívá v propojení bezpečnostního kontextu mezi LTE Evolved Packet System (EPS) a zastaralou okruhově přepínanou jádrovou sítí. Protože LTE používá jiné procedury ověření a dohody na klíči (EPS [AKA](/mobilnisite/slovnik/aka/)) zaměřené na paketově přepínanou doménu, CTS-PIN poskytuje samostatný přihlašovací údaj specificky pro scénáře přechodu (fallback). Funguje nezávisle na bezpečnostních klíčích LTE a zajišťuje, že ověření pro okruhově přepínané služby může proběhnout, i když primární bezpečnostní kontext EPS není přímo přenositelný do MSC 2G/3G. Toto oddělení bezpečnostních domén je klíčové pro zachování robustní ochrany napříč různorodými síťovými technologiemi.

Klíčové komponenty zapojené do fungování CTS-PIN zahrnují USIM v UE (který PIN ukládá a provádí kryptografické výpočty), HLR/HSS (který PIN ukládá a generuje autentizační vektory) a MSC (který řídí proces ověření typu výzva-odpověď). Specifikace zajišťuje, že CTS-PIN je používán s algoritmy kompatibilními s ověřováním GSM nebo UMTS, jako jsou varianty COMP128. Jeho implementace je povinná pro UE a sítě podporující CSFB, aby se zabránilo neoprávněnému přístupu k okruhově přepínaným prostředkům a zajistila kontinuita služby pro hlasové hovory při přechodu sítí z 3G na 4G.

## K čemu slouží

CTS-PIN byl vytvořen, aby vyřešil bezpečnostní mezeru zavedenou funkcí Circuit Switched FallBack (CSFB) ve verzi 3GPP Release 8. Jelikož byly LTE sítě nasazovány jako čistě paketově přepínané pro data a hlas (přes IMS/VoLTE), raná nasazení často postrádala plné pokrytí IMS, což vyžadovalo přechod (fallback) na zastaralé okruhově přepínané sítě pro hlasové hovory. Nicméně, nativní autentizační mechanismus LTE (EPS AKA) nebyl přímo kompatibilní s autentizačními protokoly používanými v okruhově přepínaných jádrech 2G/3G. Bez vyhrazeného přihlašovacího údaje, jako je CTS-PIN, by se UE přecházející na GSM nebo UMTS nemohlo bezpečně ověřit, což by mohlo vést k odmítnutí služby nebo závislosti na slabších, síťově specifických bezpečnostních řešeních.

Hlavní problém, který CTS-PIN řeší, je umožnění zabezpečeného a standardizovaného ověření uživatele při přechodu mezi paketově přepínanou doménou LTE a zastaralými okruhově přepínanými doménami. Před jeho zavedením mohli operátoři používat méně bezpečné metody nebo povolovat neověřený přístup během přechodu (fallback), což ohrožovalo integritu sítě. CTS-PIN poskytuje konzistentní, kryptograficky robustní tajemství, které je zřízeno v USIM a síťové databázi, a zajišťuje, že pouze oprávnění účastníci mohou během CSFB přistupovat k okruhově přepínaným službám. To bylo obzvláště důležité během přechodné fáze vývoje sítí, kdy LTE a infrastruktury 2G/3G koexistovaly po mnoho let.

Historicky vycházela motivace z potřeby zachovat zpětnou kompatibilitu a kontinuitu služby pro hlas, který zůstal kritickým zdrojem příjmů pro operátory. Definováním CTS-PIN ve specifikacích 3GPP zajistilo, že se bezpečnost nezhorší při využívání stávajících investic do okruhově přepínaných sítí, a tím usnadnilo plynulejší migraci na LTE. Vyřešilo to omezení předchozích přístupů, kdy bylo ověření vázáno výhradně na nativní doménu každé síťové technologie, což vytvářelo izolované celky bránící plynulé mobilitě.

## Klíčové vlastnosti

- Umožňuje zabezpečené ověření uživatele během Circuit Switched FallBack (CSFB) do sítí 2G/3G
- Uložen jako sdílené tajemství v USIM a síťovém HLR/HSS
- Používán se zastaralými autentizačními algoritmy GSM/UMTS (např. COMP128)
- Funguje nezávisle na bezpečnostních klíčích a procedurách LTE EPS
- Zabraňuje neoprávněnému přístupu k okruhově přepínaným prostředkům při mobilitě mezi RAT
- Zajišťuje kontinuitu služby pro hlasové hovory v raných nasazeních LTE postrádajících IMS/VoLTE

## Související pojmy

- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [CTS-PIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts-pin/)

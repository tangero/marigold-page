---
slug: "boic"
url: "/mobilnisite/slovnik/boic/"
type: "slovnik"
title: "BOIC – Barring of Outgoing International Calls"
date: 2025-01-01
abbr: "BOIC"
fullName: "Barring of Outgoing International Calls"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/boic/"
summary: "BOIC je doplňková služba v sítích GSM/UMTS/LTE/5G, která umožňuje účastníkům nebo operátorům zabránit uskutečnění odchozích mezinárodních hovorů. Poskytuje mechanismus pro kontrolu nákladů na hovory,"
---

BOIC je doplňková služba v mobilních sítích, která umožňuje účastníkům nebo operátorům zakázat odchozí mezinárodní hovory za účelem kontroly nákladů, vynucení tarifních plánů a prevence podvodů.

## Popis

Barring of Outgoing International Calls (BOIC) je standardizovaná doplňková služba definovaná v rámci 3GPP, která funguje na servisní vrstvě jádra sítě. Její funkce spočívá v zachycení požadavku na sestavení hovoru od účastníka a aplikaci kontrolní logiky na základě volaného čísla. Službu typicky spravuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) v GSM/UMTS nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v systémech LTE/5G, který uchovává profil účastníka včetně stavu aktivace BOIC. Při pokusu o uskutečnění hovoru iniciovaného mobilním zařízením se Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo IP Multimedia Subsystem (IMS) Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) dotáže HLR/HSS, aby ověřilo, zda je BOIC pro daného účastníka aktivní. Pokud je aktivní, síť analyzuje volané číslice podle mezinárodního číslovacího formátu (např. čísla začínající prefixem '+' nebo mezinárodním přístupovým kódem jako '00'). Pokud je číslo identifikováno jako mezinárodní cíl, sestavení hovoru je ukončeno a volající straně je poskytnuto upozornění (např. hlášení nebo tón).

Architektonická implementace zahrnuje úzkou interakci mezi entitami řízení hovoru (MSC, MSC Server, CSCF) a úložišti dat o účastnících (HLR/HSS). Servisní logika je provedena během počáteční fáze směrování hovoru. Mezi klíčové komponenty patří bod servisního řízení (HLR/HSS), bod servisního přepojování (MSC/CSCF provádějící detekci a dotaz) a signalizační protokoly přenášející dotaz, jako je Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) pro okruhově spínané domény nebo Diameter pro služby založené na IMS. Služba BOIC může být nastavena na úrovni jednotlivého účastníka, což umožňuje individuální kontrolu, a může být také aplikována jako síťová politika pro specifické skupiny účastníků, jako jsou předplacení uživatelé nebo firemní účty s omezeným oprávněním k mezinárodnímu volání.

Role BOIC přesahuje pouhé blokování hovorů; služba je integrována do širší sady služeb zákazu hovorů (např. [BAOC](/mobilnisite/slovnik/baoc/), BOIC-exHC), které společně tvoří komplexní soubor nástrojů pro správu služeb. Její provoz je transparentní pro rádiovou přístupovou síť (RAN), protože se jedná o funkci jádra sítě a servisní vrstvy. Služba podporuje jak zákaz zavedený operátorem (např. pro prevenci podvodů nebo nezaplacené faktury), tak zákaz vyžádaný účastníkem (např. prostřednictvím [USSD](/mobilnisite/slovnik/ussd/) kódů nebo zákaznické podpory za účelem kontroly využití, což je zvláště užitečné pro rodiče spravující telefon dítěte nebo cestující, kteří se chtějí vyhnout roamingovým poplatkům). V moderních sítích založených na IMS může být logika BOIC vynucována také Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) nebo jinými aplikačními servery, aplikujícím stejné principy na hovory Voice over LTE (VoLTE) a Voice over NR (VoNR).

## K čemu slouží

BOIC byl zaveden k řešení několika provozních a komerčních výzev v mobilních sítích. Primárně slouží jako mechanismus kontroly nákladů pro účastníky i síťové operátory. Pro účastníky, zejména v éře vysokých cen mezinárodního volání, poskytl způsob, jak proaktivně zabránit náhodným nebo neoprávněným mezinárodním hovorům, které by mohly vést k neočekávaně vysokým účtům. To bylo zvláště důležité pro firemní účty, sdílené telefony a rodiče spravující rodinné tarify. Pro operátory je BOIC klíčovým nástrojem pro správu kreditu a prevenci podvodů. Umožňuje operátorům zakázat mezinárodní volání pro účastníky s neuhrazenými dluhy nebo podezřením na podvodnou činnost, čímž omezuje finanční riziko.

Historicky, před zavedením takových standardizovaných doplňkových služeb, byla kontrola typů hovorů těžkopádnější a často vyžadovala manuální zásah zákaznické podpory nebo složité konfigurace ústředen. Standardizace BOIC v 3GPP Release 5, jako součást širších rámců služeb Intelligent Network (IN) a Customised Applications for Mobile network Enhanced Logic (CAMEL), poskytla jednotnou, škálovatelnou a vzdáleně spravovatelnou metodu. Vyřešila omezení základního, všeobecného zákazu hovorů tím, že umožnila podrobnou kontrolu nad specifickými kategoriemi hovorů (mezinárodní hovory). Tato granularita umožnila flexibilnější nabídku služeb a lepší zákaznickou zkušenost, protože uživatelé mohli zakázat drahé mezinárodní hovory a přitom stále uskutečňovat tuzemské a místní hovory.

Vznik služby byl také motivován regulatorními a konkurenčními faktory. V některých regionech jsou operátoři povinni nabízet nástroje pro kontrolu výdajů. Navíc, jak se mobilní služby globálně rozšiřovaly a roaming se stal běžnějším, rostlo riziko 'šoku z účtu' z mezinárodních hovorů (včetně hovorů uskutečněných v roamingu). BOIC spolu s příbuznými službami, jako je Barring of Outgoing International Calls except those directed to the Home PLMN Country (BOIC-exHC), poskytl technické řešení pro zmírnění tohoto rizika, což posílilo důvěru účastníků a snížilo stížnosti na zákaznické podpoře související s fakturačními spory.

## Klíčové vlastnosti

- Zabraňuje uskutečnění hovorů na mezinárodní číselné formáty
- Integruje se s HLR/HSS pro správu profilu účastníka
- Může být aktivována/deaktivována účastníkem prostřednictvím USSD nebo operátorem prostřednictvím OSS
- Funguje napříč okruhově spínanou (CS) a IMS hlasovou doménou
- Poskytuje zachycení a ukončení sestavení hovoru s upozorněním uživatele
- Podporuje jak zákaz vynucený operátorem, tak zákaz vyžádaný účastníkem

## Související pojmy

- [BAOC – Barring of All Outgoing Calls](/mobilnisite/slovnik/baoc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [BOIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/boic/)

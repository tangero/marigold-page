---
slug: "npi"
url: "/mobilnisite/slovnik/npi/"
type: "slovnik"
title: "NPI – Numbering Plan Identifier"
date: 2025-01-01
abbr: "NPI"
fullName: "Numbering Plan Identifier"
category: "Identifier"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/npi/"
summary: "Kód používaný v telekomunikacích k identifikaci konkrétního číslovacího plánu (např. E.164, E.212) přidruženého k volanému nebo účastnickému číslu. Je klíčový pro správné směrování hovorů a identifika"
---

NPI je kód používaný k identifikaci konkrétního číslovacího plánu přidruženého k číslu, což je klíčové pro správné směrování hovorů a identifikaci účastníků napříč sítěmi a mezinárodními hranicemi.

## Popis

Identifikátor číslovacího plánu (NPI) je základním parametrem v telekomunikačních signalizačních protokolech, zejména v kontextu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) a Integrated Services Digital Network User Part ([ISUP](/mobilnisite/slovnik/isup/)). Jedná se o číselný kód, který doprovází volané číslo nebo identifikátor účastníka a specifikuje typ číslovacího plánu, do kterého dané číslo patří. Toto rozlišení je zásadní, protože různé typy čísel (např. telefonní čísla, identity mobilních účastníků, čísla pro data) mají odlišná strukturální pravidla a v síti se používají k různým účelům. NPI umožňuje síťovým prvkům, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), správně interpretovat následující číslice.

V praxi je NPI přenášen v konkrétních informačních prvcích signalizačních zpráv. Například v MAP operacích, jako je Send Routing Information nebo Update Location, je Mobile Subscriber [ISDN](/mobilnisite/slovnik/isdn/) Number ([MSISDN](/mobilnisite/slovnik/msisdn/)) nebo International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) doprovázen příslušným NPI. Mezi běžné standardizované hodnoty patří 1 pro číslovací plán E.164/ISDN (používaný pro MSISDN), 3 pro číslovací plán E.212 (používaný pro IMSI) a 8 pro národní číslovací plány. Příjemní síťový uzel tento kód použije ke správné analýze následujícího řetězce číslic, čímž zajistí, že číslo určené pro mezinárodní volání není zaměněno za identitu mobilního účastníka, což by vedlo k chybám ve směrování.

Z architektonického hlediska NPI funguje na aplikační vrstvě signalizačního zásobníku SS7. Je klíčovou součástí globální interoperability telekomunikačních sítí a umožňuje bezproblémovou interakci mezi pevnými, mobilními a IP sítěmi. Jeho role přesahuje základní nastavení hovoru a zahrnuje doručování SMS, aktivaci doplňkových služeb a postupy zákonného odposlechu. Důsledné používání hodnot NPI, jak je definováno ve standardech jako ITU-T Q.713 a 3GPP TS 29.002, zajišťuje, že číslo pocházející ze sítě jednoho operátora může být správně pochopeno a zpracováno sítí jiného operátora, a to i v jiné zemi nebo technologické doméně.

## K čemu slouží

NPI byl vytvořen k řešení základního problému nejednoznačnosti čísel v propojených telekomunikačních sítích. Jak se sítě vyvíjely z jednoduchých národních pevných systémů na komplexní globální hybridy pevných, mobilních a datových sítí, mohl jediný řetězec číslic představovat více věcí: telefonní číslo, identifikátor mobilního účastníka, adresu datové sítě nebo privátní síťové rozšíření. Bez jasného identifikátoru mohly síťové ústředny číslo špatně interpretovat, což vedlo k chybnému směrování hovorů, neúspěšným transakcím a snížené kvalitě služeb.

Historicky fungovaly rané telekomunikační systémy v izolaci a interpretace čísel byla často implicitní, založená na kontextu konkrétní sítě nebo ústředny. Tento přístup selhal s příchodem digitální signalizace (SS7) a potřebou automatického mezinárodního propojení. Standardizace různých číslovacích plánů ITU-T (E.164 pro telefonii, E.212 pro mobilní identity) vytvořila strukturovaný svět, ale byl potřebný mechanismus k signalizaci, *který* plán je použit pro jakékoli dané číslo ve zprávě. NPI poskytuje tuto explicitní signalizaci a funguje jako metadatový štítek pro samotné číslo.

Tato explicitní identifikace řeší kritické problémy interoperability. Umožňuje například gateway MSC rozlišit mezi IMSI (používaným pro autentizaci účastníka a aktualizaci polohy) a MSISDN (používaným pro směrování hovorů), když jsou obě přítomny v signalizačním provozu. Umožňuje správné zpracování přenesených čísel a usnadňuje integraci negeografických číselných rozsahů. V podstatě je NPI základním prvkem umožňujícím spolehlivé, automatizované a globální směrování, na kterém moderní telekomunikace závisí, a řeší tak omezení implicitní, na kontextu závislé analýzy čísel, která předcházela standardizovaným signalizačním systémům.

## Klíčové vlastnosti

- Explicitní identifikace číslovacího plánu přidruženého k řetězci číslic
- Standardizované číselné kódy definované ITU-T a 3GPP (např. 1 pro E.164, 3 pro E.212)
- Přenášen v klíčových informačních prvcích signalizačních zpráv MAP a ISUP
- Zásadní pro správnou analýzu a interpretaci identifikátorů účastníků a volaných čísel
- Umožňuje interoperabilitu mezi různými typy sítí (pevné, mobilní, IP) a přes administrativní hranice
- Podporuje širokou škálu služeb včetně směrování hovorů, SMS a doplňkových služeb

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [NPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/npi/)

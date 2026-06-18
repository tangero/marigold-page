---
slug: "rev"
url: "/mobilnisite/slovnik/rev/"
type: "slovnik"
title: "REV – Reverse Charging"
date: 2025-01-01
abbr: "REV"
fullName: "Reverse Charging"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rev/"
summary: "REV je služební funkce, která umožňuje volané straně zaplatit za hovor místo volajícího. Běžně se používá pro bezplatná nebo reklamní čísla. Firmám umožňuje hradit komunikační náklady zákazníkům, čímž"
---

REV je služební funkce, která umožňuje volané straně, například firmě, zaplatit za hovor místo volajícího.

## Popis

Reverse Charging (REV) je funkce telekomunikační služby definovaná v 3GPP TS 29.163 a dalších specifikacích, která umožňuje, aby volaná strana (příjemce) hradila poplatky za hovor namísto volající strany (volajícího). Tato funkce je typicky implementována v jádru sítě a zahrnuje signalizaci mezi volající a volanou sítí za účelem vyjednání a aplikace dohody o zpětném účtování. REV funguje v rámci architektur Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) nebo IP Multimedia Subsystem (IMS), kde servisní logika určuje odpovědnost za účtování na základě profilů účastníků a servisních smluv.

Z architektonického hlediska zahrnuje REV komponenty jako Service Control Point ([SCP](/mobilnisite/slovnik/scp/)) v systémech založených na IN nebo Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) v IMS, které interagují se systémy účtování, jako je Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) nebo Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). Při zahájení hovoru vysílá výchozí síť signalizační zprávu (např. v [ISUP](/mobilnisite/slovnik/isup/) nebo [SIP](/mobilnisite/slovnik/sip/)) indikující žádost o zpětné účtování. Koncová síť tuto žádost ověří vůči servisnímu předplatnému volané strany a odpoví přijetím nebo odmítnutím. Pokud je žádost přijata, jsou generovány záznamy o účtování pro fakturaci volané strany, často s použitím specifických identifikátorů účtování a tarifů.

Klíčové komponenty zahrnují spouštěče účtování ve funkci Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) nebo Mobile Switching Center (MSC), které vyvolávají servisní logiku REV, a fakturační systémy, které zpracovávají převedené poplatky. Technologie funguje tak, že modifikuje standardní procedury navázání hovoru tak, aby zahrnovaly indikátory zpětného účtování, jako je Reverse Charging Indicator v ISUP nebo specifické hlavičky SIP v IMS. Tím se zajistí, že se subjekt účtování přepne z volajícího na volaného, což podporuje služby jako bezplatná linka (např. 800 čísla), kde firmy platí za příchozí hovory, aby podpořily kontakt se zákazníky.

Role REV v síti zasahuje do různých servisních scénářů, včetně služeb s prémiovým tarifem, kde se náklady sdílejí, nebo reklamních kampaní, kde společnosti hradí náklady na hovory. V moderních sítích se REV integruje s rámci řízení politik a účtování (PCC), aby umožnila dynamické účtování na základě podmínek v reálném čase. Vývoj směrem k 5G a VoLTE/VoNR přizpůsobil REV plně IP prostředím při zachování interoperability se staršími systémy a podpoře nových servisních modelů. Celkově je REV flexibilní mechanismus účtování, který usnadňuje inovativní obchodní modely a vylepšené uživatelské služby.

## K čemu slouží

REV byl zaveden za účelem podpory obchodních modelů, kdy volaná strana, například společnost nebo poskytovatel služeb, chce platit komunikační náklady, aby přilákala zákazníky nebo poskytovala služby s přidanou hodnotou. Před REV bylo účtování převážně na straně volajícího, což omezovalo možnosti bezplatného nebo reklamního volání. Tato funkce řeší problém umožnění služeb typu bezplatná linka a podobně, kdy firmy absorbují poplatky za hovory, aby zlepšily dostupnost a zapojení zákazníků.

Historicky REV vznikl v pevné telefonii s bezplatnými čísly a byl přijat do mobilních sítí jako součást možností IN v éře 2G/3G. Odstraňuje omezení tradičního účtování tím, že umožňuje flexibilní fakturační dohody, usnadňuje provoz zákaznických servisních linek, horkých linek a marketingových kampaní. Vytvoření REV ve standardech 3GPP bylo motivováno požadavky operátorů a podniků na standardizované mechanismy zpětného účtování napříč různými sítěmi a technologiemi.

V kontextu 3GPP standardizace REV od Release 8 a dále zajistila interoperabilitu mezi sítěmi GSM, UMTS a IMS a podporu bezproblémového poskytování služeb. Řeší provozní výzvy, jako jsou složitá vyúčtování a nedostatek kontroly účtování v reálném čase. Tím, že umožňuje modely placené volanou stranou, REV rozšiřuje nabídku služeb, zvyšuje provoz směřující k firmám a přizpůsobuje se vývojovým trendům v komunikaci směrem k zákaznicky orientovanému účtování ve službách VoIP a 5G.

## Klíčové vlastnosti

- Umožňuje volané straně hradit poplatky za hovor místo volající strany
- Podporuje služby bezplatných a bezúplatných čísel (např. 800 čísel)
- Integruje se s architekturami IN a IMS pro řízení služeb
- Používá standardizovanou signalizaci pro vyjednávání zpětného účtování (např. ISUP, SIP)
- Poskytuje možnosti účtování v reálném čase prostřednictvím integrace s OCS/OFCS
- Usnadňuje reklamní a zákaznické servisní obchodní modely

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [REV na 3GPP Explorer](https://3gpp-explorer.com/glossary/rev/)

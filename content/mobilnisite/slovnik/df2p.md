---
slug: "df2p"
url: "/mobilnisite/slovnik/df2p/"
type: "slovnik"
title: "DF2P – Delivery Function 2 for GPRS"
date: 2016-01-01
abbr: "DF2P"
fullName: "Delivery Function 2 for GPRS"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/df2p/"
summary: "DF2P je funkce jádra sítě v GPRS, která zajišťuje doručování mobilně-terminovaných zpráv bod-bod (MT-PP). Komunikuje s centrem služby krátkých zpráv (SMSC), aby zajistila spolehlivé doručení zpráv do"
---

DF2P je funkce jádra sítě GPRS odpovědná za doručování mobilně-terminovaných zpráv bod-bod (MT-PP) rozhraním ke SMSC a správu pokusů o doručení.

## Popis

Doručovací funkce 2 pro [GPRS](/mobilnisite/slovnik/gprs/) (DF2P) je standardizovaný síťový prvek definovaný v architektuře 3GPP, konkrétně pro službu General Packet Radio Service (GPRS). Funguje jako součást mechanismu doručování služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) pro mobilně-terminované zprávy bod-bod. Architektonicky se DF2P nachází v rámci Gateway GPRS Support Node (GGSN) nebo může být implementována jako samostatná síťová entita, která komunikuje jak s GGSN, tak s centrem služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)). Jejím hlavním úkolem je fungovat jako zprostředkovatel, který přijímá SMS zprávy určené pro mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) od SMSC prostřednictvím protokolu [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) a předává je přes infrastrukturu sítě GPRS.

DF2P funguje tak, že vytváří komunikační cestu mezi okruhově přepínaným světem SMS a paketově přepínaným jádrem GPRS. Když má SMSC zprávu pro účastníka připojeného k GPRS, odešle ji do DF2P. DF2P následně dotazuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo příslušnou databázi, aby zjistila aktuální obsluhující GGSN účastníka a stav kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)). Pokud je mobilní stanice dostupná a má aktivní PDP kontext, DF2P přepošle krátkou zprávu do GGSN, která ji pak doručí do mobilní stanice přes zavedené paketové datové spojení pomocí protokolů jako [GTP](/mobilnisite/slovnik/gtp/) (GPRS Tunnelling Protocol).

Klíčovým provozním aspektem DF2P je její odpovědnost za hlášení stavu doručení a mechanismy opakování. Pokud je mobilní stanice dočasně nedostupná (např. mimo dosah, vypnutá), DF2P zprávu uloží a zahájí následné pokusy o doručení na základě nastavených časovačů a logiky opakování. Informuje SMSC o konečném výsledku doručení – úspěch, selhání nebo čekání – a zajišťuje tak správnou funkci čekání na zprávy a upozorňování v SMSC. To vyžaduje, aby DF2P udržovala stavové informace pro každou transakci se zprávou a komunikovala s HLR pro aktualizace dostupnosti účastníka.

Funkce se integruje s několika klíčovými protokoly. Její rozhraní směrem k SMSC typicky používá MAP (Mobile Application Part) přes SS7 (Signalling System No. 7) nebo IP-based SIGTRAN, přenášející operace specifické pro SMS, jako je MT-ForwardSM. Směrem k jádru GPRS používá GTP-C (GTP Control) pro ověření kontextu a může aktivovat síť k vytvoření potřebného paketového datového kontextu, pokud není aktivní. To činí z DF2P klíčový konvergenční bod, který umožňuje efektivní doručování SMS, dědičné okruhově přepínané služby, přes moderní paketově přepínané sítě bez nutnosti, aby mobil přepnul zpět do okruhově přepínaného režimu.

## K čemu slouží

DF2P byla vytvořena, aby umožnila doručování zpráv služby krátkých zpráv (SMS) do mobilních stanic, které jsou připojeny k síti General Packet Radio Service (GPRS) a tuto síť používají. Před zavedením GPRS se SMS doručovaly výhradně přes řídicí kanály okruhově přepínané sítě. Zavedení GPRS, paketově přepínané datové služby, znamenalo, že mobilní stanice mohly být ve stavu, kdy neposlouchaly okruhově přepínané stránkovací kanály, a byly tak nedostupné pro tradiční doručování SMS. DF2P tento problém řeší poskytnutím vyhrazené cesty pro doručování SMS přes paketově přepínané jádro, čímž zajišťuje kontinuitu této kritické zprávové služby při vývoji sítí.

Historický kontext představuje přechod ze sítí GSM 2G, které byly primárně okruhově přepínané pro hlas a SMS, na sítě GPRS 2.5G, které zavedly 'vždy zapojená' paketová data. Klíčovým konstrukčním cílem bylo umožnit účastníkům používat paketové datové služby, aniž by jim chyběly příchozí SMS zprávy. DF2P řešila omezení předchozího přístupu, kde bylo doručování SMS pevně svázáno se stavem správy mobility v okruhově přepínané doméně. Oddělením doručování SMS a jeho směrováním přes paketové jádro umožnila DF2P efektivnější využití síťových zdrojů a lepší uživatelský zážitek, protože mobilní stanice nemusela neustále monitorovat více rádiových kanálů.

Dále DF2P standardizovala rozhraní mezi SMSC – často starším systémem – a novým paketovým jádrem GPRS. To bylo klíčové pro síťové operátory zavádějící GPRS, protože jim to umožnilo integraci s existující infrastrukturou SMSC bez větších úprav. Řešila problém, jak může síťová entita navržená pro okruhově přepínané signalizace (SMSC) komunikovat s paketově přepínanou přenosovou sítí a využívat ji k doručení své zátěže, čímž chránila investice do infrastruktury SMS a zároveň umožnila modernizaci sítě.

## Klíčové vlastnosti

- Zajišťuje doručování mobilně-terminovaných SMS zpráv bod-bod přes GPRS
- Komunikuje s centrem služby krátkých zpráv (SMSC) pomocí protokolu MAP
- Dotazuje HLR pro informace o směrování a stavu účastníka
- Předává SMS zprávy do GGSN pro doručení přes GTP
- Spravuje ukládání zpráv a pokusy o opakování pro nedostupné účastníky
- Poskytuje SMSC hlášení o stavu doručení

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [DF2P na 3GPP Explorer](https://3gpp-explorer.com/glossary/df2p/)

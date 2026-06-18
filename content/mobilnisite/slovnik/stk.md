---
slug: "stk"
url: "/mobilnisite/slovnik/stk/"
type: "slovnik"
title: "STK – SIM Application Toolkit"
date: 2025-01-01
abbr: "STK"
fullName: "SIM Application Toolkit"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/stk/"
summary: "Standard umožňující SIM kartě hostovat aplikace a komunikovat s mobilním zařízením a sítí. Umožňuje síťovým operátorům a poskytovatelům služeb nabízet přidané služby, jako jsou nabídkové informační sl"
---

STK je standard, který umožňuje SIM kartě hostovat aplikace a komunikovat s mobilním zařízením a sítí za účelem poskytování přidaných služeb přímo ze SIM karty.

## Popis

[SIM](/mobilnisite/slovnik/sim/) Application Toolkit (STK) je soubor příkazů a procedur definovaných 3GPP, který umožňuje aplikacím umístěným na UICC (Universal Integrated Circuit Card), běžně známé jako SIM karta, proaktivně komunikovat s mobilním zařízením ([ME](/mobilnisite/slovnik/me/)), uživatelem a sítí. Zásadně transformuje SIM kartu z pasivního autentizačního modulu na aktivní platformu pro poskytování služeb. Architektura je založena na modelu klient-server, kde SIM karta funguje jako klientská aplikační platforma a síť poskytuje podporu na straně serveru prostřednictvím Bearer Independent Protocol (BIP) nebo [SMS](/mobilnisite/slovnik/sms/) jako přenosových mechanismů.

STK funguje tak, že definuje řadu proaktivních příkazů, které může SIM karta odesílat do mobilního telefonu. Tyto příkazy instruují telefon, aby provedl konkrétní akce, jako je zobrazení nabídky, přehrání tónu, odeslání SMS, navázání hovoru nebo poskytnutí informací o poloze. Telefon příkaz vykoná a vrátí odpověď (terminálovou odpověď) zpět do aplikace na SIM kartě. Tuto interakci spravuje interpret STK v telefonu, který musí být v souladu se specifikacemi 3GPP, aby příkazy správně rozuměl a vykonával. Mezi klíčové komponenty patří proaktivní SIM karta, interpret STK v ME a síťová infrastruktura pro [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) provizionování a přenos dat.

Jeho role v síti je klíčová pro bezpečné, operátorem řízené nasazování služeb. Protože aplikační logika sídlí na zabezpečeném prvku (SIM/UICC), nabízí důvěryhodné prostředí pro provádění citlivých operací, jako jsou finanční transakce. STK umožňuje služby jako nabídky na bázi SIM karty pro kontrolu zůstatku, dobíjení kreditu, aktivaci služeb a informační služby. Také usnadňuje OTA správu, což operátorům umožňuje vzdáleně instalovat, personalizovat, aktualizovat nebo mazat aplikace na SIM kartě bez nutnosti fyzického přístupu, což výrazně snižuje provozní náklady a umožňuje rychlé uvedení služeb na trh.

## K čemu slouží

STK byl vytvořen, aby překonal omezení raných mobilních sítí, kde byla servisní logika pevně svázána s koncovým zařízením, což síťovým operátorům ztěžovalo a zpomalovalo nasazování nových služeb. Před STK vyžadovala jakákoli nová funkce její implementaci ve firmwaru od výrobců telefonů, což vedlo k roztříštěné dostupnosti a dlouhé době uvedení na trh. [SIM](/mobilnisite/slovnik/sim/) karta byla používána pouze pro autentizaci a ukládání kontaktů.

Hlavní problém, který STK řeší, je poskytnutí standardizované, bezpečné a na zařízení nezávislé platformy pro servisní inovace řízené síťovým operátorem. Přesunutím aplikační logiky na SIM kartu získali operátoři přímou kontrolu nad poskytováním služeb a mohli zajistit konzistentní uživatelský zážitek napříč různými modely telefonů. To bylo obzvláště důležité pro zavádění bezpečných služeb mobilního obchodu, bankovnictví a informačních služeb v éře před chytrými telefony. Jeho vytvoření bylo motivováno potřebou zpeněžit síť nad rámec hlasových hovorů a základních [SMS](/mobilnisite/slovnik/sms/), což umožnilo nový ekosystém přidaných služeb přímo dostupných z hlavní nabídky mobilního zařízení.

## Klíčové vlastnosti

- Proaktivní příkazy SIM karty pro řízení chování telefonu
- Zabezpečené prováděcí prostředí v rámci UICC/SIM
- Provizionování a správa aplikací přes vzdušné rozhraní (OTA)
- Bearer Independent Protocol (BIP) pro přenos dat založený na IP
- Podpora nabídkových uživatelských rozhraní ze SIM karty
- Integrace se službami SMS a USSD pro spouštění služeb a přenos dat

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [STK na 3GPP Explorer](https://3gpp-explorer.com/glossary/stk/)

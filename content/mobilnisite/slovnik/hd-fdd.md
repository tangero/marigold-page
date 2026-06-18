---
slug: "hd-fdd"
url: "/mobilnisite/slovnik/hd-fdd/"
type: "slovnik"
title: "HD-FDD – Half-Duplex Frequency Division Duplex"
date: 2025-01-01
abbr: "HD-FDD"
fullName: "Half-Duplex Frequency Division Duplex"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hd-fdd/"
summary: "Duplexní režim, ve kterém přenosy v uplinku a downlinku používají různé frekvence (FDD), ale UE nemůže vysílat a přijímat současně. Pro přepínání mezi Tx a Rx využívá ochranný interval, což snižuje sl"
---

HD-FDD je duplexní režim, ve kterém uplink a downlink používají oddělené frekvence, ale zařízení nemůže vysílat a přijímat současně, což vyžaduje ochranný interval pro přepínání a snižuje složitost.

## Popis

Half-Duplex Frequency Division Duplex (HD-FDD) je duplexní metoda používaná v celulárních systémech, jako jsou LTE a NR, kde komunikace v uplinku a downlinku probíhají na oddělených, spárovaných frekvenčních pásmech (jako ve standardním [FDD](/mobilnisite/slovnik/fdd/)), ale User Equipment (UE) nemusí vysílat a přijímat současně. Místo toho UE pracuje ve frekvenčním spektru FDD časově děleným způsobem, střídavě přechází mezi fázemi vysílání a příjmu. To vyžaduje ochranný interval, během kterého se rádiový obvod UE přepíná mezi režimem vysílání a příjmu.

Na architektonické úrovni má HD-FDD UE zjednodušené [RF](/mobilnisite/slovnik/rf/) přední části ve srovnání s plně duplexním FDD (FD-FDD) UE. FD-FDD UE vyžaduje vysoce výkonný duplexer – filtr, který izoluje silný výstupní vysílací signál od citlivého příchozího přijímaného signálu, protože oba jsou aktivní současně na sousedních frekvencích. HD-FDD UE může používat jednodušší přepínač nebo méně výkonný duplexer, protože vysílací a přijímací cesty nejsou nikdy aktivní ve stejný okamžik. Toto snížení nákladů a složitosti RF komponent je hlavní výhodou.

Z pohledu protokolu musí základnová stanice (eNodeB v LTE, gNB v NR) vědět, která UE podporují HD-FDD. Síťové plánování musí zajistit, že pro HD-FDD UE neplánuje přenos v uplinku ve stejnou dobu, kdy je plánován příjem v downlinku. V praxi norma umožňuje UE definovat specifický HD-FDD vzor, nebo jej může síť nakonfigurovat pomocí signalizace vyšší vrstvy. Doba přepínání mezi stavy Tx a Rx je specifikována v RF požadavcích (např. TS 36.101, 38.101) a zabírá malou část podrámce, která je vyhrazena jako ochranný interval. Tento ochranný interval představuje nepatrnou ztrátu ve spektrální účinnosti, která je vyvážena významným snížením ceny UE. Provoz HD-FDD je zvláště relevantní pro LTE a NR v pásmech tradičně používaných pro FDD systémy, což umožňuje nízkonákladovým IoT zařízením (jako LTE-M, NB-IoT v FDD pásmech) a nízkorozpočtovým telefonům využívat FDD spektrum.

## K čemu slouží

HD-FDD bylo zavedeno za účelem snížení ceny a spotřeby energie UE, zejména pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) a nízkorozpočtová koncová zařízení, při zachování možnosti provozu ve [FDD](/mobilnisite/slovnik/fdd/) spektru. Tradiční FD-FDD UE vyžadují drahé a fyzicky rozměrné duplexní filtry, které poskytují dostatečnou izolaci mezi blízko umístěnými vysílacími a přijímacími frekvencemi. Tyto komponenty tvoří významnou část nákladů na [RF](/mobilnisite/slovnik/rf/) část.

Uvolněním požadavku na simultánní vysílání a příjem HD-FDD odstraňuje potřebu tohoto vysoce výkonného duplexeru. Místo něj lze použít levnější přepínač nebo filtr. To bylo klíčovým faktorem pro zařízení LTE Cat-1 a později Cat-M1 (LTE-M) a NB-IoT, která jsou navržena pro ultra nízkou cenu a dlouhou výdrž baterie pro IoT aplikace. Umožnilo to nasazení těchto technologií v existujících FDD pásmech vlastněných operátory po celém světě, aniž by cena UE musela zůstat nepřiměřeně vysoká. Kompromisem je mírné snížení špičkových přenosových rychlostí a flexibility plánování, protože UE nemůže být 'neustále v naslouchání' downlinku během vysílání. Pro mnoho IoT aplikací s přerušovaným přenosem malých objemů dat je však tento kompromis zcela přijatelný a vede k optimalizovaným celkovým nákladům na vlastnictví.

## Klíčové vlastnosti

- UE pracuje ve spárovaném FDD spektru, ale nevysílá a nepřijímá současně
- Využívá časové dělení v rámci FDD pásem, což vyžaduje přepínání Tx/Rx
- Odstraňuje potřebu vysoce výkonného RF duplexeru, čímž snižuje cenu a velikost UE
- Vyžaduje ochranné intervaly pro RF přepínání, což mírně snižuje spektrální účinnost
- Síťové plánování se musí vyhnout překrývajícím se přiřazením UL a DL pro HD-UE
- Klíčový faktor pro nízkonákladová LTE a NR IoT zařízení (např. LTE-M, NB-IoT) ve FDD pásmech

## Související pojmy

- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [HD-FDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hd-fdd/)

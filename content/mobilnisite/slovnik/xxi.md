---
slug: "xxi"
url: "/mobilnisite/slovnik/xxi/"
type: "slovnik"
title: "XXI – 1447.9 - 1462.9 MHz"
date: 2025-01-01
abbr: "XXI"
fullName: "1447.9 - 1462.9 MHz"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/xxi/"
summary: "Konkrétní frekvenční pásmo definované 3GPP pro provoz UTRA (UMTS Terrestrial Radio Access) v režimu TDD. Toto pásmo, označené jako pásmo 22, se používá pro mobilní služby s časovým duplexem (Time Divi"
---

XXI je označení 3GPP pro pásmo 22, konkrétní nepárové UTRA TDD frekvenční pásmo od 1447,9 do 1462,9 MHz používané pro mobilní služby s časovým duplexem (Time Division Duplex).

## Popis

Termín 'XXI' v terminologii 3GPP označuje konkrétní rádiové frekvenční pásmo definované pro provoz [UTRA](/mobilnisite/slovnik/utra/) v režimu časového duplexu (Time Division Duplex, [TDD](/mobilnisite/slovnik/tdd/)). Specifikuje frekvenční rozsah od 1447,9 MHz do 1462,9 MHz, který poskytuje celkem 15 MHz nepárového spektra. Toto pásmo je standardizováno jako 3GPP pásmo 22, TDD pásmo používané primárně pro UMTS ([TD-SCDMA](/mobilnisite/slovnik/td-scdma/)) a potenciálně pro nasazení LTE-TDD, ačkoli jeho globální adopce byla ve srovnání s [FDD](/mobilnisite/slovnik/fdd/) pásmy omezená.

V TDD systému, jaký se používá v pásmu 22, je stejný blok spektra (1447,9–1462,9 MHz) využíván pro přenosy v uplinku i downlinku, oddělené v časové doméně. Základnová stanice a uživatelské zařízení (UE) vysílají ve střídajících se časových slotech podle nakonfigurované TDD rámcové struktury. Pro UMTS TDD (TD-SCDMA) to zahrnuje specifické alokace časových slotů a synchronizační procedury definované v UTRA specifikacích. Parametry fyzické vrstvy, včetně kanálového rastru, povolených šířek kanálů (např. 1,6 MHz nosné pro TD-SCDMA) a [RF](/mobilnisite/slovnik/rf/) požadavků, jsou podrobně popsány v 3GPP TS 25.141 pro testování shody základnových stanic.

Z perspektivy síťové architektury vyžaduje nasazení pásma 22 NodeB podporující TDD (pro 3G) nebo eNodeB (pro 4G LTE-TDD). Středně-frekvenční charakteristiky tohoto pásma (kolem 1,45 GHz) nabízejí rovnováhu mezi pokrytím a kapacitou; poskytuje lepší šíření než vyšší pásma jako 2,6 GHz, ale menší pokrytí než pásma pod 1 GHz, jako je 800 MHz. Plánování sítě pro TDD pásma musí pečlivě spravovat časovou synchronizaci napříč všemi buňkami v síti, aby se předešlo interferenci mezi uplinkem a downlinkem a aby efektivně alokovala časové sloty na základě asymetrie provozu (např. více downlink slotů pro datově náročné použití).

Provoz v pásmu 22 vyžaduje, aby se základnová stanice a UE řídily striktním schématem časového předstihu (timing advance) a ochranné periody, aby kompenzovaly zpoždění šíření a zajistily, že se časové sloty nepřekrývají. Pro LTE-TDD, pokud je nasazeno, by se používala jedna ze standardizovaných TDD konfigurací pro uplink-downlink. Ačkoli není tak široce nasazeno jako některá jiná pásma, pásmo 22 představuje důležitý zdroj nepárového spektra, který může být využit pro mobilní širokopásmový přístup, zejména v regionech nebo operátory, kteří mají přístup k této konkrétní frekvenční alokaci. Jeho definice zajišťuje, že výrobci zařízení mohou vyrábět terminály a infrastrukturu, které jsou interoperabilní a shodné s globálními standardy, a to i pro regionálně specifická pásma.

## K čemu slouží

Standardizace pásma XXI (1447,9–1462,9 MHz) jako pásma 22 byla motivována potřebou začlenit další [TDD](/mobilnisite/slovnik/tdd/) spektrum do rámce 3GPP, aby podpořila rostoucí mobilní datový provoz a poskytla flexibilitu operátorům s alokacemi nepárového spektra. Na rozdíl od [FDD](/mobilnisite/slovnik/fdd/), které vyžaduje párové bloky spektra, může TDD fungovat v nepárových pásmech, což jej činí vhodným pro spektrum, které není symetricky dostupné. Rozsah kolem 1,4 GHz byl v některých regionech identifikován jako dostupný pro mobilní služby a 3GPP poskytlo standardizovanou definici pásma, aby umožnilo jeho využití.

Předtím se TDD operace pro 3G soustředily převážně na jiná pásma (jako pásmo 34 na 2 GHz). Definice pásma 22 rozšířila portfolio standardizovaného TDD spektra a dala regulátorům a operátorům více možností pro nasazení sítí UMTS TDD ([TD-SCDMA](/mobilnisite/slovnik/td-scdma/)) nebo později LTE-TDD. Tím se řešil problém fragmentace spektra tím, že se zajistilo, že zařízení pro tento konkrétní frekvenční rozsah budou vyráběna podle společného standardu, což podporuje konkurenci a snižuje náklady.

Dále vytvoření pásma 22 sloužilo účelu budoucí připravenosti nasazení sítí. Jeho zahrnutí do UTRA specifikací od verze Rel-9 výše zajistilo, že toto spektrum může být použito nejen pro 3G TD-SCDMA, ale také, v principu, pro 4G LTE-TDD, protože pásmo je také součástí specifikací pásem E-UTRA. To umožňuje přeměnu technologie (refarming), kdy by operátor mohl potenciálně migrovat služby z 3G na 4G v rámci stejného pásma. Ačkoli jeho použití není globální, pásmo 22 reprezentuje princip komplexní standardizace spektra, který zajišťuje, že prakticky jakákoli alokovaná mobilní frekvence může být podporována v rámci ekosystému 3GPP s interoperabilním zařízením.

## Klíčové vlastnosti

- Frekvenční rozsah: 1447,9 MHz až 1462,9 MHz, poskytující 15 MHz nepárového spektra pro provoz TDD
- Standardizováno jako 3GPP pásmo 22 pro UTRA TDD (a použitelné pro LTE-TDD)
- Používá časový duplex (Time Division Duplex), kde uplink a downlink sdílejí stejné frekvence ve střídajících se časových slotech
- Středně-frekvenční pásmo nabízející rovnováhu charakteristik pokrytí a kapacity
- Požadavky na testování shody základnových stanic definovány v 3GPP TS 25.141
- Podporuje šířky kanálů vhodné pro TD-SCDMA (např. 1,6 MHz) a LTE-TDD

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [XXI na 3GPP Explorer](https://3gpp-explorer.com/glossary/xxi/)

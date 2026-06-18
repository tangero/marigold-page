---
slug: "fdn"
url: "/mobilnisite/slovnik/fdn/"
type: "slovnik"
title: "FDN – Fixed Dialling Number"
date: 2025-01-01
abbr: "FDN"
fullName: "Fixed Dialling Number"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fdn/"
summary: "Služba pro účastníka umožňující pouze hovory na předem definovaný seznam čísel, čímž omezuje odchozí hovory. Používá se pro rodičovskou kontrolu, správu firemních telefonů a kontrolu nákladů tím, že b"
---

FDN je služba pro účastníka, která omezuje odchozí hovory na předem definovaný seznam čísel, spravovaný přes USIM a vynucovaný mobilním zařízením.

## Popis

Fixed Dialling Number (FDN) je služba orientovaná na účastníka definovaná ve specifikacích 3GPP pro sítě GSM, UMTS a LTE/5GS. Funguje jako mechanismus zákazu hovorů, který omezuje odchozí hovory, které může uživatel z mobilního zařízení uskutečnit, pouze na ta čísla, která jsou výslovně uvedena v seznamu FDN uloženém na modulu [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) nebo [SIM](/mobilnisite/slovnik/sim/) kartě. Primárním místem vynucení je samo mobilní zařízení ([ME](/mobilnisite/slovnik/me/)), které konzultuje tento seznam uložený na USIM předtím, než povolí pokračování v sestavení hovoru. Když se uživatel pokusí uskutečnit hovor, softwarová vrstva řízení hovorů v ME porovná vytočené číslo se záznamy v seznamu FDN. Pokud je nalezena shoda (nebo pokud je číslo na definovaném seznamu 'nouzových' výjimek od operátora nebo regulátora), je hovor povolen k pokračování prostřednictvím běžné signalizace do sítě. Pokud shoda není nalezena, ME pokus o hovor lokálně ukončí a síť není vůbec kontaktována, čímž se zabrání případným poplatkům nebo neoprávněnému použití.

Architektura FDN je úzce integrována s aplikační sadou nástrojů USIM a modemovým softwarem zařízení. Seznam FDN je uložen jako vyhrazený soubor ([EF](/mobilnisite/slovnik/ef/)_FDN) v rámci souborového systému USIM, chráněný přístupovou podmínkou, typicky PIN2. Správa seznamu – přidávání, mazání nebo úprava záznamů – se provádí přes Man-Machine Interface ([MMI](/mobilnisite/slovnik/mmi/)) telefonu, který po úspěšném ověření PIN2 posílá do USIM příkazy [APDU](/mobilnisite/slovnik/apdu/) pro aktualizaci souboru EF_FDN. Tento návrh zajišťuje bezpečnost a přenositelnost seznamu omezení; seznam se přesouvá spolu s SIM kartou a uplatňuje stejná pravidla bez ohledu na použitý telefon (za předpokladu, že telefon FDN podporuje). Služba je nezávislá na jádru sítě; jedná se o funkci na straně klienta, přestože síťoví operátoři mohou počáteční seznam zřídit nebo službu povolit/zakázat prostřednictvím protokolů Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)).

V širší architektuře služeb FDN interaguje s dalšími službami zákazu hovorů, jako je Barring of All Outgoing Calls ([BAOC](/mobilnisite/slovnik/baoc/)) a Barring of Outgoing International Calls (BOIC), ale je podrobnější. Zatímco síťové služby zákazu jsou vynucovány Mobile Switching Center (MSC) nebo funkcemi Access and Mobility Management Function (AMF)/Session Management Function (SMF) na základě profilu účastníka, FDN poskytuje řízení definované uživatelem nebo správcem na úrovni zařízení. Její role je klíčová pro konkrétní případy použití: umožňuje rodičům omezit dětský telefon pouze na kontakty, firmám omezit firemní zařízení na obchodní čísla a pomáhá předcházet podvodům uzamčením odcizených SIM karet na omezenou sadu čísel. Přestože se jedná o starší službu GSM, FDN zůstává relevantní a podporovaná v 5G zařízeních, což dokládá trvalou potřebu jednoduchých mechanismů omezení hovorů vynucovaných zařízením.

## K čemu slouží

FDN byla vytvořena pro uspokojení potřeby podrobného, uživatelem řízeného omezení hovorů přímo na mobilním zařízení. Před jejím zavedením byla kontrola hovorů primárně službou síťového operátora (jako zákaz hovorů) nebo jednoduchou funkcí telefonu jako zámek klávesnice, které byly buď příliš široké, nebo snadno obejitelné. Zejména ze strany firemních a rodičovských uživatelů rostla poptávka po metodě, která by omezila používání zařízení na konkrétní sadu čísel za účelem kontroly nákladů a zajištění vhodného použití. FDN tento problém vyřešila využitím bezpečnosti a přenositelnosti SIM karty pro uložení bílé listiny, díky čemuž se omezení stalo trvalým a vázaným na identitu účastníka, nikoli na konkrétní, potenciálně nahraditelné zařízení.

Motivace vycházela z komercializace mobilních telefonů a nástupu zpoplatněných služeb a mezinárodního roamingu, kde nežádoucí hovory mohly vést k významným výdajům. Pro firmy představovalo poskytování mobilních telefonů zaměstnancům riziko neoprávněných osobních nebo mezinárodních hovorů. FDN poskytla přímočarý administrativní nástroj ke zmírnění tohoto finančního rizika. Na spotřebitelském trhu nabídla rodičům klid tím, že jim umožnila nakonfigurovat telefon pro dítě pouze s nezbytnými kontakty, čímž zvýšila bezpečnost. Technologie využívá stávající bezpečnostní model USIM (PIN2) k ochraně konfigurace, což zajišťuje, že seznam povolených čísel může upravovat pouze oprávněná osoba (např. rodič nebo IT administrátor).

Její pokračující zařazení do každého vydání 3GPP až po Rel-19 podtrhuje její užitečnost jako základní telefonní služby. Zatímco síťové politiky a řešení správy mobilních zařízení (MDM) se vyvinuly a nabízejí sofistikovanější kontroly, FDN zůstává jednoduchým, standardizovaným a všeobecně podporovaným záložním mechanismem, který funguje bez závislosti na síti. Řeší základní problém základní autorizace odchozích hovorů způsobem, který je interoperabilní napříč sítěmi a zařízeními – princip, který zůstává cenný i v pokročilých 5G systémech.

## Klíčové vlastnosti

- Omezení hovorů na bílou listinu čísel uloženou na USIM
- Vynucování na straně klienta mobilním zařízením (ME)
- Správa prostřednictvím rozhraní MMI chráněného PIN2
- Uložení ve vyhrazeném souboru EF_FDN na USIM
- Přenositelnost mezi různými telefony se stejným USIM
- Souběžná existence se síťovými službami zákazu od operátora

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)
- [EF – Elementary File](/mobilnisite/slovnik/ef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [FDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdn/)

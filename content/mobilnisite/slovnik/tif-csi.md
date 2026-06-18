---
slug: "tif-csi"
url: "/mobilnisite/slovnik/tif-csi/"
type: "slovnik"
title: "TIF-CSI – Translation Information Flag for Camel Subscription Information"
date: 2025-01-01
abbr: "TIF-CSI"
fullName: "Translation Information Flag for Camel Subscription Information"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tif-csi/"
summary: "TIF-CSI je příznak indikátoru služby CAMEL používaný v sítích GSM/UMTS k signalizaci, zda je pro spuštění služby Inteligentní sítě (IN) vyžadována překladová informace o volaném čísle. Zajišťuje správ"
---

TIF-CSI je příznak indikátoru služby CAMEL, který signalizuje, zda je pro spuštění služby Inteligentní sítě vyžadována překladová informace o volaném čísle.

## Popis

Translation Information Flag for Camel Subscription Information (TIF-CSI) je specifický parametr v rámci sady dat [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information ([CSI](/mobilnisite/slovnik/csi/)) uložené v domovském zářiči polohy ([HLR](/mobilnisite/slovnik/hlr/)). CAMEL (Customised Applications for Mobile network Enhanced Logic) je standard 3GPP pro služby Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) v GSM a UMTS, umožňující operátorské služby jako předplacené hovory, screening hovorů nebo [VPN](/mobilnisite/slovnik/vpn/). TIF-CSI funguje jako logický příznak (boolean) asociovaný s profilem CAMEL služeb účastníka. Pokud je nastaven, nařizuje navštívené ústředně [MSC](/mobilnisite/slovnik/msc/) ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo bránové ústředni MSC ([GMSC](/mobilnisite/slovnik/gmsc/)), že překladová informace – například získaná z databáze přenosnosti čísel (NPDB) nebo jiné analýzy číslování – musí být získána pro volané číslo před vyvoláním jakékoli servisní logiky CAMEL, jako je spuštění detekčního bodu Initial DP. Tím je zajištěno, že servisní logika obdrží správné, případně přenesené nebo přeložené, cílové číslo pro přesné zpracování.

Architektonická role TIF-CSI je klíčová v řetězci sestavování hovoru a vyvolávání služeb. Při uskutečnění mobilního odchozího nebo příchozího hovoru se MSC dotazuje HLR na účastníkovo CSI. Pokud je TIF-CSI přítomen a nastaven, je MSC povinna provést překladový dotaz, často přes signalizační rozhraní SS7 k SCP nebo vyhrazené databázi, aby vyřešila volané číslo. Tento krok překladu typicky řeší scénáře jako přenosnost mobilních čísel (MNP), kdy volané číslo již nemusí být asociováno se svou původní sítí nebo směrovací předponou. Teprve po získání tohoto přeloženého směrovacího čísla (Mobile Station Roaming Number, MSRN, pro příchozí hovory, nebo konečného směrovacího čísla) MSC pokračuje ve spuštění služby CAMEL odesláním zprávy Initial DP do prostředí CAMEL Service Environment (CSE) nebo Service Control Point (SCP), včetně přeloženého čísla jako parametru.

Klíčové komponenty interagující s TIF-CSI zahrnují HLR (který jej ukládá), MSC nebo GMSC (které jej interpretují a podle něj jednají) a externí překladové databáze nebo SCP. Jeho fungování je definováno v rámci signalizačních procedur CAMEL Application Part (CAP). Přítomnost příznaku zabraňuje nesprávnému provádění služeb; například předplacená služba by mohla nesprávně vypočítat tarify na základě nepřeloženého, potenciálně nesměrovatelného čísla. Tím, že zajistí provedení překladu jako prvního kroku, TIF-CSI udržuje integritu logiky služeb IN, podporuje regulatorní požadavky jako přenosnost čísel a umožňuje složité scénáře směrování hovorů. Je to základní prvek pro zajištění správné funkce služeb založených na CAMEL v moderních, interoperabilních sítích, kde je překlad čísel běžný.

## K čemu slouží

TIF-CSI byl zaveden, aby vyřešil kritickou mezeru v raných implementacích CAMEL: potřebu integrovat spouštění služeb Inteligentní sítě s síťovým překladem čísel, což bylo primárně hnuto zavedením přenosnosti mobilních čísel (MNP). Před jeho zavedením by se servisní logika CAMEL spouštěla na základě volaných číslic tak, jak byly přijaty od volající strany. Avšak s MNP volané číslo již nemuselo odpovídat původní síťové směrovací informaci. Spuštění služby jako předplacené účtování nebo přesměrování hovoru na základě nepřeloženého čísla mohlo vést k nesprávnému chování služby, neúspěšnému směrování hovoru nebo chybám v účtování. TIF-CSI poskytuje standardizovaný mechanismus k vynucení provedení překladu čísla jako povinného kroku před vyvoláním CAMEL, čímž zajišťuje, že servisní logika používá přesné, směrovatelné cílové informace.

Vytvoření TIF-CSI bylo motivováno regulatorními a konkurenčními tlaky vyžadujícími přenosnost čísel, což si vyžádalo úpravy procedur zpracování hovorů v sítích. Bez příznaku jako je TIF-CSI by operátoři potřebovali proprietární, neinteroperabilní řešení nebo by riskovali poruchu služeb CAMEL ve scénářích s přenesenými čísly. Standardizací tohoto příznaku v 3GPP Release 4 bylo zajištěno konzistentní chování napříč MSC a HLR různých dodavatelů, což usnadnilo bezproblémový roaming a interoperabilitu služeb. Vyřešil problém sekvencování – zajištění, že překlad (funkce síťového směrování) logicky předchází provedení servisní logiky (funkce aplikační vrstvy). Toto oddělení zájmů je zásadní pro robustní architekturu IN.

Dále TIF-CSI podporuje více než jen MNP; může být použit pro jakoukoli službu vyžadující překlad čísel, jako je překlad bezplatných čísel, výběr operátora nebo změny v národním číslovacím plánu. Jeho účel sahá až k budoucí odolnosti služeb CAMEL vůči vyvíjejícím se číslovacím schématům. Oddělením požadavku na překlad od konkrétní servisní logiky umožňuje síťovým operátorům zavádět nové překladové databáze nebo pravidla bez nutnosti modifikace každé CAMEL servisní aplikace na SCP. TIF-CSI je tedy klíčovým prvkem umožňujícím flexibilní, spolehlivé a regulatorním požadavkům vyhovující služby Inteligentní sítě v ekosystémech 2G a 3G.

## Klíčové vlastnosti

- Logický indikátor (boolean) v rámci CAMEL Subscription Information (CSI) uloženého v HLR
- Nařizuje provedení překladu čísla (např. přes dotaz MNP) před spuštěním CAMEL Initial DP
- Zajišťuje, že servisní logika CAMEL obdrží správné, směrovatelné cílové číslo
- Kritická podpora pro regulatorní požadavky přenosnosti mobilních čísel (MNP)
- Zabraňuje chybám v účtování a poruchám služeb u přenesených čísel
- Umožňuje oddělení překladových funkcí od provádění servisní logiky

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [TIF-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tif-csi/)

---
slug: "nv"
url: "/mobilnisite/slovnik/nv/"
type: "slovnik"
title: "NV – Name and Value Pair"
date: 2025-01-01
abbr: "NV"
fullName: "Name and Value Pair"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nv/"
summary: "Základní konstrukt datového modelování hojně využívaný ve specifikacích správy sítí 3GPP (zejména pro správu výkonu). Představuje jediný měřitelný atribut (Name – název) a jeho přidružená data (Value"
---

NV (Name and Value) je základní konstrukt datového modelování, který představuje jediný měřitelný atribut a jeho přidruženou hodnotu. Používá se pro strukturované shromažďování a reportování metrik výkonu sítě a konfiguračních parametrů v rámci správy podle 3GPP.

## Popis

Dvojice Název a Hodnota (NV) je základní datová struktura v rámci frameworku Telecommunication Management ([TM](/mobilnisite/slovnik/tm/)) podle 3GPP, specifikovaná primárně v technických specifikacích řady 32. Slouží jako atomická jednotka informace pro reprezentaci dat správy. Koncepčně se dvojice NV skládá ze dvou složek: 'Name' (název), což je jedinečný identifikátor konkrétního atributu, parametru nebo metriky, a 'Value' (hodnota), což je samotná datová instance přidružená k tomuto názvu. 'Name' typicky odpovídá definovanému atributu spravovaného objektu nebo čítači měření výkonu ([PM](/mobilnisite/slovnik/pm/)). 'Value' může být různých datových typů, jako je celé číslo, desetinné číslo, řetězec, čítač, ukazatel nebo složitější struktura, v závislosti na definici atributu.

Architektonicky se dvojice NV používají na rozhraních mezi síťovými prvky ([NE](/mobilnisite/slovnik/ne/)), systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) a systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)). Jsou datovou náplní managementových protokolů a formátů souborů používaných pro sběr a reportování dat správy výkonu (PM). Například při hromadném přenosu souborů s měřeními výkonu (specifikováno v 32.307 a 32.373) jsou data PM organizována jako série dvojic NV uvnitř záznamů měření. Každý záznam odpovídá konkrétnímu měřícímu období a instanci spravovaného objektu (např. buňce) a obsahuje více dvojic NV reprezentujících čítače jako 'Počet úspěšných zahájení hovoru', 'Úroveň rušení v uplinku' nebo 'Objem paketových dat'. 'Name' poskytuje kontext, zatímco 'Value' poskytuje naměřenou veličinu.

Jak to funguje v praxi, zahrnuje generování, sběr a zpracování. Síťové prvky interně udržují čítače a ukazatele pro různé indikátory výkonu. Na konci měřícího období NE naformátuje tato data do strukturované reportu sestávajícího z dvojic NV. Tento report je pak přenesen do EMS/NMS pomocí protokolů jako [FTAM](/mobilnisite/slovnik/ftam/), [SFTP](/mobilnisite/slovnik/sftp/) nebo rozhraní založených na [CORBA](/mobilnisite/slovnik/corba/). Systém správy používá metadatový slovník nebo informační model (definovaný např. ve specifikacích 32.303 a 32.306) k interpretaci každého 'Name' – k pochopení jeho sémantického významu, datového typu a jednotek. Systém pak může 'Value' agregovat, korelovat a analyzovat pro diagnostiku chyb, plánování kapacity a zajištění služeb. Jednoduchost a flexibilita dvojice NV z ní činí univerzální stavební prvek pro reprezentaci různorodých managementových informací napříč různými síťovými technologiemi (2G, 3G, 4G, 5G) v rámci jednotného paradigmatu správy.

## K čemu slouží

Koncept dvojice NV byl vytvořen k řešení problému standardizace reprezentace a výměny dat správy v telekomunikačních sítích s více dodavateli a technologiemi. Rané systémy správy sítí často používaly proprietární datové formáty, což ztěžovalo integraci a centralizovanou analýzu výkonu a bylo nákladné. Byla zde potřeba společného, flexibilního a rozšiřitelného způsobu modelování a přenosu jakékoliv části managementové informace – ať už šlo o konfigurační parametr, stavový indikátor nebo čítač výkonu.

Jeho motivace vychází z principů objektově orientovaných managementových modelů, jako jsou ty definované ITU-T a TM Forum. Dvojice NV poskytuje obecný kontejner, který může reprezentovat jakýkoliv atribut spravovaného objektu. Tím řeší omezení rigidního reportování s pevným formátem. Oddělením identifikátoru atributu (Name) od jeho dat (Value) lze systém snadno rozšiřovat: nové metriky lze přidat definováním nových 'Name' bez změny základní struktury reportování nebo logiky parsování. To je klíčové pro rychlé zavádění nových síťových funkcí a měření napříč releasy 3GPP.

Historicky jeho formální přijetí v 3GPP Release 8 a podrobná specifikace v řadě 32 poskytly základní kámen pro automatizovanou správu výkonu. Umožnilo definici standardizovaných souborů měření výkonu (PM souborů), které mohly být vygenerovány jakýmkoliv kompatibilním NE a zpracovány jakýmkoliv kompatibilním NMS. Tato interoperabilita snížila provozní náklady a umožnila operátorům získat jednotný přehled o výkonu sítě. Trvalá přítomnost dvojice NV v následujících releasech, včetně 5G, podtrhuje její úspěch jako základního konstruktu datového modelování pro správu a orchestraci sítě, podporujícího jak tradiční OAM, tak moderní paradigmata správy NFV/SDN.

## Klíčové vlastnosti

- Atomická datová struktura sestávající z identifikátoru atributu (Name) a jeho přidružených dat (Value).
- Používá se jako primární formát pro data měření výkonu (PM) v hromadném reportování soubory (např. PM soubory).
- Podporuje více datových typů pro Value (celé číslo, desetinné číslo, čítač, řetězec atd.).
- Umožňuje rozšiřitelné modely managementových informací; nové metriky se přidávají definováním nových Name.
- Umožňuje interoperabilitu více dodavatelů na rozhraních správy sítě.
- Definováno ve specifikacích 3GPP TM (32.303, 32.306, 32.307, 32.373, 32.376) pro konzistentní implementaci.

## Definující specifikace

- **TS 32.303** (Rel-9) — Notification IRP CORBA Solution Set
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.307** (Rel-9) — Notification IRP SOAP Solution Set
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set

---

📖 **Anglický originál a plná specifikace:** [NV na 3GPP Explorer](https://3gpp-explorer.com/glossary/nv/)

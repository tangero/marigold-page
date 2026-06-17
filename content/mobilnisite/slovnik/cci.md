---
slug: "cci"
url: "/mobilnisite/slovnik/cci/"
type: "slovnik"
title: "CCI – Capability/Configuration1 Identifier"
date: 2025-01-01
abbr: "CCI"
fullName: "Capability/Configuration1 Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cci/"
summary: "CCI je jedinečný identifikátor používaný v sítích 3GPP pro reprezentaci konkrétních schopností nebo konfigurací uživatelského zařízení (UE). Umožňuje efektivní signalizaci tím, že sítě mohou odkazovat"
---

CCI je jedinečný identifikátor používaný v sítích 3GPP pro efektivní odkazování na předdefinované sady schopností nebo konfigurací uživatelského zařízení (UE), čímž se snižuje signalizační režie a urychluje navazování spojení.

## Popis

Identifikátor schopností/konfigurací (Capability/Configuration1 Identifier – CCI) je standardizovaný mechanismus ve specifikacích 3GPP, který poskytuje kompaktní reprezentaci schopností nebo konfigurací uživatelského zařízení (UE). Namísto přenosu rozsáhlých seznamů jednotlivých schopností během síťových procedur slouží CCI jako odkaz na předdefinovanou sadu schopností, které rozumí jak UE, tak síť. Tento identifikátor je obzvláště cenný ve scénářích, kde by častá výměna informací o schopnostech vytvářela nadměrnou signalizační režii, jako například při předávání spojení (handover), opětovném navazování spojení nebo při připojování více UE s podobnými schopnostmi k síti.

CCI funguje prostřednictvím standardizovaného mapování mezi konkrétními sadami schopností a jim odpovídajícími hodnotami identifikátoru. Když UE podporuje konkrétní kombinaci schopností, která odpovídá předdefinovanému profilu, může v signalizačních zprávách použít přidruženou hodnotu CCI namísto vypisování každé schopnosti jednotlivě. Síť udržuje databázi nebo porozumění tomu, co každá hodnota CCI reprezentuje, což jí umožňuje interpretovat schopnosti UE na základě tohoto jediného identifikátoru. Tento systém vyžaduje pečlivou koordinaci mezi standardizačními snahami a síťovou implementací, aby bylo zajištěno konzistentní porozumění napříč různými síťovými elementy a implementacemi UE.

V praktické implementaci se CCI používá v různých procedurách 3GPP včetně signalizace řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), správy mobility a správy relací. Identifikátor se typicky objevuje ve zprávách jako RRC Connection Setup Complete, Handover Request nebo jiných signalizačních výměnách týkajících se schopností. Konkrétní hodnoty CCI a jim odpovídající sady schopností jsou definovány v technických specifikacích 3GPP, což zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů. Tato standardizace je klíčová pro zachování konzistentního chování sítě a zabránění chybné interpretaci schopností UE v různých nasazeních sítě.

Architektura podporující CCI zahrnuje, že jak strana UE, tak síťová strana udržují synchronizované porozumění mapování CCI. Na straně UE musí zařízení určit, která hodnota CCI nejlépe reprezentuje jeho aktuální schopnosti na základě jeho hardwarové konfigurace, softwarových funkcí a provozního režimu. Na síťové straně musí elementy rádiové přístupové sítě (RAN) a funkce jádra sítě umět interpretovat přijatou hodnotu CCI a aplikovat příslušné síťové politiky, alokace zdrojů a povolování funkcí na základě identifikované sady schopností. Tato koordinace zajišťuje, že sítě mohou optimalizovat svůj provoz pro různé typy UE bez nutnosti rozsáhlého individuálního hlášení schopností.

Role CCI přesahuje pouhou indikaci schopností a zahrnuje také aspekty konfigurace. V některých implementacích může identifikátor reprezentovat nejen to, jaké schopnosti UE má, ale také jak jsou tyto schopnosti nakonfigurovány nebo které konkrétní provozní režimy jsou aktivní. Tato dvojí povaha činí CCI obzvláště cenným ve složitých síťových scénářích, kde jak dostupnost schopností, tak aktuální konfigurační stav ovlivňují, jak by síť měla s UE interagovat. Identifikátor tedy slouží jako komplexní zkratka pro aktuální technický stav UE z pohledu jak hardwarových schopností, tak softwarové konfigurace.

## K čemu slouží

CCI byl zaveden, aby řešil rostoucí složitost signalizace schopností UE v sítích 3GPP. Jak se mobilní zařízení vyvíjela a začala podporovat stále rozmanitější soubory funkcí včetně více rádiových přístupových technologií, pokročilých kodeků, bezpečnostních funkcí a schopností specifických pro aplikace, tradiční přístup přenosu úplných seznamů schopností se stal neefektivním. Tyto rozsáhlé výměny schopností spotřebovávaly významné rádiové zdroje, prodlužovaly dobu navazování spojení a vytvářely režii zpracování jak pro UE, tak pro síťové elementy. CCI poskytl standardizované řešení tohoto problému tím, že umožnil kompaktní reprezentaci běžných kombinací schopností.

Historický kontext vývoje CCI spočívá v přechodu od relativně jednoduchých zařízení 2G/3G ke složitějším terminálům 4G a 5G s rozsáhlými soubory funkcí. Rané mobilní sítě mohly zvládat výměnu schopností prostřednictvím relativně krátkých zpráv, ale jak počet možných schopností exponenciálně rostl, byl nutný efektivnější mechanismus. CCI to řešil tím, že umožňoval sítím a UE odkazovat na předdefinované profily schopností, což dramaticky snížilo velikost signalizačních zpráv při zachování úplné informace o schopnostech UE.

Předchozí přístupy trpěly několika omezeními, která CCI konkrétně řeší. Úplný výpis schopností vyžadoval významnou šířku pásma, což bylo obzvláště problematické v scénářích s omezenými rádiovými zdroji nebo při častých událostech mobility. Režie zpracování parsování a interpretace dlouhých seznamů schopností také ovlivňovala výkon sítě a životnost baterie UE. Kromě toho nekonzistentní formáty hlášení schopností mezi různými implementacemi UE vytvářely problémy s interoperabilitou. CCI tyto výměny standardizoval a zároveň optimalizoval jak efektivitu signalizace, tak požadavky na zpracování, což jej činí obzvláště cenným pro sítě obsluhující velký počet zařízení s podobnými profily schopností.

## Klíčové vlastnosti

- Kompaktní reprezentace sad schopností UE
- Snížená signalizační režie při výměně informací o schopnostech
- Standardizované mapování mezi identifikátory a profily schopností
- Podpora jak indikace schopností, tak reprezentace konfigurace
- Použití v rámci více procedur 3GPP včetně RRC a správy mobility
- Interoperabilita mezi zařízeními různých dodavatelů prostřednictvím standardizovaných hodnot

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [CCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cci/)

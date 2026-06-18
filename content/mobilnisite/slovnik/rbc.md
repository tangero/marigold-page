---
slug: "rbc"
url: "/mobilnisite/slovnik/rbc/"
type: "slovnik"
title: "RBC – Radio Bearer Control"
date: 2026-01-01
abbr: "RBC"
fullName: "Radio Bearer Control"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rbc/"
summary: "Radio Bearer Control (RBC) je základní funkcí v rámci architektury správy rádiových prostředků (RRM) v sítích 3GPP. Je zodpovědná za zřizování, udržování, konfiguraci a uvolňování rádiových přenosovýc"
---

RBC je funkce správy rádiových prostředků (Radio Resource Management) zodpovědná za zřizování, udržování, konfiguraci a uvolňování rádiových přenosových kanálů (radio bearers) s odpovídající kvalitou služeb (QoS) pro přenos uživatelských dat a signalizace.

## Popis

Radio Bearer Control (RBC) je klíčovou součástí vrstvy správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), která je primárně vykonávána řadičem rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS a stanicí gNB v LTE a NR. Řídí životní cyklus rádiových přenosových kanálů (radio bearers), což jsou logická spojení mapovaná na fyzické rádiové prostředky. Rádiový přenosový kanál je charakterizován sadou atributů, včetně třídy provozu, garantované přenosové rychlosti, maximální přenosové rychlosti, pořadí doručování a poměru chyb [SDU](/mobilnisite/slovnik/sdu/), které definují jeho profil QoS. Mezi funkce RBC patří zřizování, rekonfigurace a uvolňování přenosových kanálů, spouštěné událostmi jako zahájení relace, předávání spojení (handover) nebo změny v podmínkách sítě či požadavcích služeb.

Proces začíná, když základní síť (Core Network) prostřednictvím Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) požaduje přenosový kanál s konkrétními parametry QoS pro uživatelskou relaci. Funkce RBC v přístupové síti (RAN) vyhodnotí aktuální dostupnost rádiových prostředků, možnosti UE a požadovanou QoS, aby rozhodla, zda lze kanál přijmout. Pokud je přijat, nakonfiguruje odpovídající protokoly vrstvy 2 ([RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/)) a parametry fyzické vrstvy pro realizaci kanálu. To zahrnuje přidělení identifikátorů logických kanálů, konfiguraci režimů RLC (Transparentní, Nepotvrzovaný, Potvrzovaný) a nastavení parametrů plánování ve vrstvě MAC.

Během aktivní relace RBC průběžně sleduje výkon přenosového kanálu. Může iniciovat rekonfiguraci kanálu v reakci na události mobility (např. předání spojení), změny v charakteru provozu nebo podmínkách zatížení sítě. Například během předání spojení z jedné buňky do druhé RBC znovu zřídí přenosový kanál v cílové buňce, čímž zajistí kontinuitu služby s minimálním přerušením. Také zajišťuje uvolnění přenosových kanálů při ukončení relace nebo v důsledku selhání rádiového spoje. Interakce mezi RBC a dalšími funkcemi RRM, jako je řízení přístupu (Admission Control), plánování paketů (Packet Scheduling) a řízení předání spojení (Handover Control), je klíčová pro efektivní využití rádiových prostředků a udržování end-to-end QoS napříč přístupovou a základní sítí.

## K čemu slouží

Radio Bearer Control (RBC) existuje za účelem správy logických přenosových kanálů, které přenášejí uživatelská data a řídicí signalizaci přes rozhraní vzduchu v prostředí s omezenými a dynamickými rádiovými prostředky. Jeho primárním účelem je převést požadavky na kvalitu služeb (QoS) na úrovni služeb, přijaté od základní sítě, na konkrétní konfigurace rádiových prostředků, které může přístupová síť (RAN) implementovat. Bez RBC by síť nebyla schopna garantovat diferencovanou kvalitu služeb pro různé aplikace, jako jsou hlasové hovory, video streamování nebo prohlížení webu, což by vedlo ke špatnému uživatelskému zážitku a neefektivnímu využití spektra.

Koncept byl zaveden v 3G UMTS (Release 99) k řešení omezení 2G GSM, které nabízelo především okruhově spínaný hlas s omezenými datovými schopnostmi. GSM postrádalo sofistikovaný, dynamický systém správy přenosových kanálů pro paketová data. RBC poskytlo potřebný rámec pro podporu více souběžných přenosových kanálů s různými profily QoS pro jednoho uživatele, což umožnilo skutečné multimediální služby. Řešilo problém efektivního multiplexování provozu s různými požadavky na zpoždění, ztrátovost a propustnost na sdílené fyzické kanály, což je základním kamenem pro vývoj směrem k plně IP sítím a mobilnímu širokopásmovému připojení.

Jak se sítě vyvíjely k LTE a 5G NR, role RBC zůstala klíčová, ale její implementace se stala více distribuovanou a integrovanou s dalšími funkcemi RAN. Přechod od centralizovaného [RNC](/mobilnisite/slovnik/rnc/) v UMTS k distribuované architektuře eNB/gNB vyžadoval, aby byla funkčnost RBC vestavěna přímo do základnové stanice, což umožnilo rychlejší rozhodování a přizpůsobování se rychlým změnám kanálu. Tato evoluce byla motivována potřebou nižší latence, vyšších přenosových rychlostí a podpory výrazně rozšířené škály služeb a případů užití v 4G a 5G.

## Klíčové vlastnosti

- Zřizování a konfigurace přenosových kanálů: Vytváří a konfiguruje rádiové přenosové kanály s konkrétními atributy QoS, jako je třída provozu, přenosové rychlosti a tolerance k chybám.
- Rekonfigurace přenosových kanálů: Dynamicky upravuje parametry přenosových kanálů během aktivních relací v reakci na předání spojení, změny provozu nebo podmínky v síti.
- Uvolňování přenosových kanálů: Ukončuje rádiové přenosové kanály po dokončení relace nebo při selhání rádiového spoje, čímž uvolňuje prostředky.
- Mapování a vynucování QoS: Převádí parametry QoS základní sítě (QCI, 5QI) na konfigurace specifické pro RAN pro plánování a přizpůsobování spojení.
- Interakce s funkcemi RRM: Úzce koordinuje činnost s řízením přístupu (Admission Control), plánováním paketů (Packet Scheduling) a řízením předání spojení (Handover Control) pro holistickou správu prostředků.
- Podpora více přenosových kanálů na UE: Spravuje současně několik vyhrazených a výchozích přenosových kanálů pro jedno uživatelské zařízení (UE) za účelem podpory souběžných služeb.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [RBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/rbc/)

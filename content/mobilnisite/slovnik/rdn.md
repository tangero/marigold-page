---
slug: "rdn"
url: "/mobilnisite/slovnik/rdn/"
type: "slovnik"
title: "RDN – Relative Distinguished Name"
date: 2026-01-01
abbr: "RDN"
fullName: "Relative Distinguished Name"
category: "Identifier"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rdn/"
summary: "Součást X.500 Distinguished Name (DN), která jednoznačně identifikuje záznam v rámci jeho bezprostředního nadřazeného kontextu v hierarchickém adresáři, například objekt správy (MO) v managementu sítí"
---

RDN je součástí X.500 Distinguished Name, která jednoznačně identifikuje záznam v rámci jeho nadřazeného kontextu pomocí páru klíč-hodnota, například pro adresování objektu správy (Management Object) v sítích 3GPP.

## Popis

Relative Distinguished Name (RDN) je základním stavebním prvkem ze standardu adresářových služeb X.500, který je rozsáhle přijímán ve specifikacích managementu 3GPP pro strukturování a identifikaci spravovaných objektů. V kontextu 3GPP je každý spravovaný prostředek – například síťová funkce, hardwarová komponenta nebo logická entita jako síťový řez – reprezentován jako instance objektu správy ([MO](/mobilnisite/slovnik/mo/)) v hierarchickém stromě informací o správě ([MIT](/mobilnisite/slovnik/mit/)). Každá instance MO je jednoznačně adresována svým Distinguished Name ([DN](/mobilnisite/slovnik/dn/)), což je sekvence RDN zřetězená od kořene stromu až ke konkrétnímu MO. Samotný RDN je tvrzení atribut-hodnota, typicky jediný pár klíč-hodnota (např. `ManagedElementId=Gnb123`), který jednoznačně identifikuje MO mezi jeho sourozenci pod stejným nadřazeným MO. Například plný DN buňky gNB může být: `DN=SubNetwork=CountryA, ManagedElement=Gnb123, GNBDUFunction=1, NRCellDU=Cell456`. Zde `NRCellDU=Cell456` je RDN, který jednoznačně identifikuje tuto buňku v rámci jejího nadřazeného `GNBDUFunction`. Hierarchická struktura vynucovaná RDN umožňuje logické seskupování a efektivní navigaci. Všechna rozhraní managementu 3GPP, jako je Itf-N (northbound rozhraní) nebo služby managementu definované pro 5G, používají DN složené z RDN jako primární odkaz pro cílení konkrétních prostředků při operacích jako vytvoření, čtení, aktualizace, smazání a notifikace. Syntaxe a povolené atributy pro RDN jsou definovány ve specifikacích 3GPP Management Data ([MD](/mobilnisite/slovnik/md/)), konkrétně v TS 32.300, která poskytuje rámec pro pojmenování. Tento důsledný konvent pojmenování je klíčový pro zajištění jednoznačné komunikace mezi systémy správy (např. [NMS](/mobilnisite/slovnik/nms/), [OSS](/mobilnisite/slovnik/oss/)) a síťovými elementy nebo mezi síťovými funkcemi v architektuře založené na službách, což umožňuje přesnou konfiguraci, korelaci chyb a sledování inventáře napříč komplexní, multi-vendorovou sítí.

## K čemu slouží

Přijetí konceptu RDN/[DN](/mobilnisite/slovnik/dn/) ze standardu X.500 do managementu 3GPP (počínaje Release 8) řešilo kritickou potřebu standardizovaného, hierarchického a jednoznačného schématu pojmenování pro všechny spravované objekty v telekomunikační síti. Předchozí přístupy byly často ad-hoc nebo specifické pro dodavatele, což vedlo k nekonzistentnostem v tom, jak byly síťové prostředky identifikovány napříč různými rozhraními a systémy správy. To činilo automatizovanou správu, integraci více dodavatelů a rozsáhlou orchestraci extrémně obtížnými. Hierarchické pojmenování založené na RDN poskytuje přirozený způsob, jak modelovat reálné vztahy obsahování síťových prostředků (např. síť obsahuje podsítě, které obsahují spravované elementy, které obsahují funkce). Tato struktura není jen pro identifikaci; umožňuje výkonné operace správy jako vymezení rozsahu (aplikace operace na všechny objekty pod nadřazeným objektem) a dědičnost vlastností. Řeší problém jednoznačné identifikace milionů instancí spravovaných objektů v globální síti při zachování čitelných pro člověka a strojově zpracovatelných názvů. To je nezbytné pro funkce jako správa chyb, kde alarm musí přesně indikovat selhávající komponentu, nebo správa konfigurace, kde musí být profil řezu aplikován na konkrétní sadu síťových funkcí. Rámec RDN podporuje celou architekturu managementu 3GPP, což umožňuje implementovat automatizované, modelově řízené operace a je předpokladem pro pokročilé koncepty jako uzavřená smyčka automatizace a management založený na záměrech v 5G a dalších generacích.

## Klíčové vlastnosti

- Pár klíč-hodnota (např. `AttributeName=Hodnota`), který jednoznačně identifikuje objekt mezi jeho sourozenci
- Základní komponenta pro konstrukci hierarchického Distinguished Name (DN) spravovaného objektu
- Umožňuje logické modelování vztahů obsahování ve stromu informací o správě (MIT)
- Poskytuje jednoznačné adresování pro všechny operace správy (CRUD, notifikace)
- Definován standardy 3GPP pro zajištění konzistence napříč všemi rozhraními správy
- Podporuje vymezení rozsahu a filtrování v požadavcích služeb správy

## Definující specifikace

- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.652** (Rel-19) — UTRAN Network Resource Model (NRM) IRP Information Service
- **TS 28.655** (Rel-19) — GERAN NRM IRP Information Service
- **TS 28.658** (Rel-19) — E-UTRAN NRM IRP Information Service
- **TS 28.662** (Rel-19) — Generic RAN Network Resource Model (NRM) IRP IS
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 28.732** (Rel-19) — Transport Network NRM IRP Information Service
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention
- **TS 32.312** (Rel-19) — Generic IRP Management Information Service
- **TS 32.602** (Rel-19) — Basic Configuration Management IRP Information Service
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [RDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rdn/)

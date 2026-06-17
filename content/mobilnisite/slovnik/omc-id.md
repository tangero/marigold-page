---
slug: "omc-id"
url: "/mobilnisite/slovnik/omc-id/"
type: "slovnik"
title: "OMC-ID – Operation and Maintenance Centre Identity"
date: 2025-01-01
abbr: "OMC-ID"
fullName: "Operation and Maintenance Centre Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/omc-id/"
summary: "Identita provozního a údržbového centra (OMC-ID) je jedinečný identifikátor přiřazený OMC v rámci Evolved Packet System (EPS). Používá se v řídicích a signalizačních procedurách, zejména pro trasovací"
---

OMC-ID je jedinečný identifikátor pro provozní a údržbové centrum (Operation and Maintenance Centre) v EPS, používaný v řízení a signalizaci k jednoznačné identifikaci systému, který zahájil operaci nebo trasování.

## Popis

Identita provozního a údržbového centra (OMC-ID) je parametr definovaný v architektuře 3GPP Evolved Packet Core (EPC) počínaje Release 8. Slouží jako jedinečný identifikátor pro provozní a údržbové centrum, což je systém pro správu sítě. OMC-ID není adresou pro přenos uživatelských dat, ale používá se v rámci signalizace řídicí a managementové roviny k přiřazení řídicích akcí, jako je aktivace trasování, konkrétnímu [OMC](/mobilnisite/slovnik/omc/), které je vyžádalo.

Technicky je OMC-ID strukturován a používán v rámci rozhraní a procedur managementu. Klíčovým případem použití je funkce Trace Control and Configuration Management (TCCM). Když OMC nebo Network Manager ([NM](/mobilnisite/slovnik/nm/)) potřebuje aktivovat trasování na uživatelském zařízení (UE) nebo síťové entitě (jako je [MME](/mobilnisite/slovnik/mme/) nebo eNodeB), zahrne své OMC-ID do žádosti o aktivaci trasování. Tento identifikátor je pak propagován sítí a zahrnut do záznamů trasování. To umožňuje, aby všechna shromážděná trasovací data byla spojena zpět s původním řídicím systémem, což je zásadní pro auditování, řešení problémů a správu více OMC ve velké síti.

OMC-ID je součástí širšího rámce managementu a zabezpečení. Pomáhá rozlišovat mezi řídicími požadavky přicházejícími z různých provozních domén nebo od různých poskytovatelů služeb v roamingu. Identifikátor je typicky definován operátorem sítě a musí být jedinečný v rámci domény managementu. Jeho zařazení do standardů zajišťuje interoperabilitu mezi řídicími systémy a síťovými prvky od různých dodavatelů a poskytuje jasnou auditní stopu pro konfiguraci sítě a diagnostické aktivity.

## K čemu slouží

OMC-ID byl zaveden spolu s EPS v 3GPP Release 8, aby řešil potřebu jednoznačného přiřazení řídicích akcí v stále složitějších a vrstvených architekturách správy sítě. Jak se sítě vyvíjely z 2G/3G na LTE/EPC, řídicí systémy se staly více hierarchickými (s Element Managery, Network Managery a [OSS](/mobilnisite/slovnik/oss/)) a pro škálovatelnost nebo různé administrativní domény mohlo být nasazeno více [OMC](/mobilnisite/slovnik/omc/).

Bez jedinečného identifikátoru by bylo nemožné určit, který řídicí systém zahájil konkrétní trasování nebo změnu konfigurace, což by vedlo k provoznímu zmatku a mezerám v bezpečnostním auditu. OMC-ID to řeší označováním každé řídicí akce identitou svého zdroje. To je obzvláště kritické pro funkci trasování, která se používá pro péči o zákazníky, vyšetřování poruch a optimalizaci; znalost původu žádosti o trasování je nezbytná pro kontext a odpovědnost.

Jeho standardizace navíc podporuje interoperabilitu více dodavatelů v managementové rovině. Definováním společného parametru zajišťuje, že OMC od dodavatele A může úspěšně zahájit trasování na síťovém prvku od dodavatele B a záznamy trasování budou správně nést identifikátor zpět k vyžadujícímu systému. To podporuje otevřenější a lépe spravovatelné síťové prostředí s více dodavateli.

## Klíčové vlastnosti

- Jedinečný identifikátor pro provozní a údržbové centrum (Operations and Maintenance Centre) v rámci domény managementu EPS
- Slouží k označení původce řídicích akcí, zejména žádostí o aktivaci trasování
- Propagován v záznamech trasování, aby poskytl auditní stopu
- Podporuje správu v prostředích OSS s více dodavateli a hierarchickou strukturou
- Nezbytný pro bezpečnostní auditování a odpovědnost za změny konfigurace sítě
- Definován operátorem sítě a musí být jedinečný v rámci svého rozsahu použití

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description

---

📖 **Anglický originál a plná specifikace:** [OMC-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/omc-id/)

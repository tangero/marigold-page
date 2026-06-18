---
slug: "dcar"
url: "/mobilnisite/slovnik/dcar/"
type: "slovnik"
title: "DCAR – Data Channel Application Repository"
date: 2026-01-01
abbr: "DCAR"
fullName: "Data Channel Application Repository"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dcar/"
summary: "Úložiště a architektura pro správu aplikací využívajících 5G datové kanály. Umožňuje vyhledávání, nasazování a správu životního cyklu aplikací, které využívají rozšířené komunikační schopnosti 5G sítí"
---

DCAR je 3GPP úložiště aplikací datových kanálů (Data Channel Application Repository), což je architektura pro vyhledávání, nasazování a správu životního cyklu aplikací, které využívají rozšířené možnosti 5G datových kanálů, jako jsou nízkolatenční datové toky.

## Popis

Data Channel Application Repository (DCAR) je standardizovaná architektonická komponenta v rámci servisně orientované architektury ([SBA](/mobilnisite/slovnik/sba/)) 5G, která představuje centralizované úložiště a systém pro správu aplikací navržených pro využití 5G datových kanálů. Datový kanál je logická komunikační cesta zřízená mezi uživatelským zařízením (UE) a aplikačním serverem, která nabízí rozšířené možnosti oproti standardní IP konektivitě, jako je garantovaná kvalita služeb (QoS), ultra-spolehlivá nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) a časově citlivé síťování. DCAR funguje jako katalog a platforma pro nasazování těchto specializovaných aplikací, které mohou zahrnovat software pro řízení průmyslové automatizace nebo klienty pro imerzivní rozšířenou realitu ([XR](/mobilnisite/slovnik/xr/)).

Architektonicky je DCAR definován jako síťová funkce ([NF](/mobilnisite/slovnik/nf/)), která své schopnosti zpřístupňuje prostřednictvím servisního rozhraní, typicky založeného na [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/). Interaguje s dalšími funkcemi 5G jádra sítě, jako je funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) a funkce úložiště síťových funkcí ([NRF](/mobilnisite/slovnik/nrf/)). NEF může poskytovat zabezpečené rozhraní API pro poskytovatele aplikací třetích stran, aby mohli publikovat své aplikace pro datové kanály do DCAR. NRF umožňuje, aby bylo DCAR objevitelné ostatními síťovými funkcemi, jako je funkce pro správu relací (SMF) nebo specializovaná aplikační funkce (AF), které potřebují dotazovat nebo spouštět nasazení konkrétní aplikace. Samotné úložiště uchovává aplikační balíčky, které zahrnují binární soubory aplikace nebo kontejnerové image, metadata (jako požadované QoS profily, charakteristiky datových kanálů a schopnosti UE) a deskriptory nasazení.

Provoz DCAR zahrnuje několik klíčových procesů. Za prvé onboarding aplikace, při kterém poskytovatel aplikace publikuje aplikační balíček do úložiště prostřednictvím standardizovaných procedur. Za druhé vyhledávání aplikací, při kterém síťové funkce nebo autorizované entity mohou dotazovat DCAR, aby našly aplikace vhodné pro konkrétní kontext UE nebo scénář služby. Za třetí správu životního cyklu aplikace, která zahrnuje správu verzí, povolování/zakazování aplikací a případně spouštění vytváření instancí aplikací ve vhodných cloudových/edge prostředích. Když UE iniciuje službu vyžadující datový kanál, může síťová funkce (např. AF) požadovat informace o aplikaci z DCAR. Na základě metadat aplikace může síť následně zřídit PDU relaci nebo QoS tok s přesnými charakteristikami (latence, spolehlivost, šířka pásma) požadovanými danou aplikací, čímž zajistí optimální výkon.

Jeho role v síti je klíčová pro umožňování služeb a automatizaci. Oddělením aplikační logiky od konfigurace podkladové sítě DCAR usnadňuje dynamičtější a efektivnější využití pokročilých funkcí 5G. Umožňuje síťovým operátorům a třetím stranám nabízet specializované, na síť citlivé aplikace bez nutnosti hluboké, manuální integrace pro každou novou službu. To podporuje vizi 5G o integraci vertikálních odvětví, kde mohou být různorodé aplikace z výroby, zdravotnictví nebo automobilového průmyslu bezproblémově nasazovány a spravovány s využitím garantovaného výkonu 5G datových kanálů.

## K čemu slouží

DCAR byl vytvořen, aby řešil výzvu spojenou se správou a nasazováním rostoucího ekosystému aplikací závislých na specializovaných komunikačních schopnostech 5G sítí, konkrétně datových kanálů. Před 5G mobilní sítě primárně nabízely best-effort IP konektivitu. Zavedení 5G přineslo sofistikované mechanismy pro síťové slicing, URLLC a diferenciaci QoS, což umožnilo nové případy užití, jako je automatizace továren, vzdálená chirurgie a autonomní vozidla. Nebyl však standardizovaný způsob, jak tyto pokročilé síťové schopnosti katalogizovat, vyhledávat a asociovat s konkrétními aplikacemi, které je vyžadovaly. Nasazování aplikací bylo často manuálním, proprietárním procesem, což bránilo škálovatelnosti a interoperabilitě.

Primární problém, který DCAR řeší, je efektivní správa životního cyklu 'na síť citlivých' aplikací. Bez úložiště by každá vertikální aplikace vyžadovala vlastní integraci, aby síť informovala o svých specifických požadavcích na latenci, spolehlivost nebo šířku pásma pro zřízení datového kanálu. To vytváří provozní složitost a zpomaluje inovace služeb. DCAR poskytuje standardizované úložiště a rozhraní, které umožňuje publikovat požadavky aplikací jednou a následně je automaticky vyhledávat a používat řídicí rovinou sítě v případě potřeby. Tím se automatizuje propojení mezi záměrem aplikace a poskytováním síťových prostředků.

Jeho vytvoření bylo motivováno prací 3GPP v Release 18 na vylepšení 5G pro vertikály a průmyslový IoT, jak je dokumentováno ve specifikacích 5G Advanced. Cílem bylo vytvořit architekturu, která podporuje komerční nasazení těchto pokročilých služeb tím, že ze správy aplikací učiní nativní síťovou funkci. Poskytnutím centralizovaného referenčního bodu pro aplikace datových kanálů umožňuje DCAR síťovým operátorům nabízet platformu pro vývojáře třetích stran, čímž podporuje ekosystém inovativních služeb plně využívajících technologický pokrok 5G, a tím otevírá nové zdroje příjmů a případy užití.

## Klíčové vlastnosti

- Centralizované úložiště pro aplikační balíčky a metadata datových kanálů
- Standardizované servisní rozhraní (např. prostřednictvím NEF) pro publikaci a vyhledávání aplikací
- Schopnosti správy životního cyklu aplikací (onboarding, povolování, správa verzí)
- Asociace požadavků aplikace s konkrétními 5G QoS profily a charakteristikami datových kanálů
- Integrace s funkcemi 5G jádra sítě (NRF, NEF, SMF) pro automatizované poskytování služeb
- Podpora pro nasazení na síť citlivých aplikací v edge computing prostředích

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.392** (Rel-19) — MMTel Application Enablement
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study

---

📖 **Anglický originál a plná specifikace:** [DCAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcar/)

---
slug: "gmmrr"
url: "/mobilnisite/slovnik/gmmrr/"
type: "slovnik"
title: "GMMRR – GPRS Mobility Management Radio Resource"
date: 2025-01-01
abbr: "GMMRR"
fullName: "GPRS Mobility Management Radio Resource"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/gmmrr/"
summary: "GMMRR označuje aspekty správy rádiových prostředků integrované s procedurami správy mobility GPRS, zejména pro optimalizaci v síti GERAN (GSM/EDGE RAN). Zaměřuje se na efektivní přidělování a uvolňová"
---

GMMRR je aspekt správy rádiových prostředků v rámci správy mobility GPRS, který optimalizuje efektivní přidělování a uvolňování rádiových kanálů během událostí mobility v síti GERAN.

## Popis

[GPRS](/mobilnisite/slovnik/gprs/) Mobility Management Radio Resource (GMMRR) je koncept v rámci specifikací 3GPP, který se zabývá koordinací mezi procedurami správy mobility a správou rádiových prostředků v sítích GPRS/[EDGE](/mobilnisite/slovnik/edge/) ([GERAN](/mobilnisite/slovnik/geran/)). Zatímco [GMM](/mobilnisite/slovnik/gmm/) (GPRS Mobility Management) primárně funguje na vrstvě Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) mezi UE a [SGSN](/mobilnisite/slovnik/sgsn/), jeho procedury nevyhnutelně ovlivňují rádiovou přístupovou síť. GMMRR zahrnuje mechanismy a optimalizace pro to, jak jsou rádiové prostředky – konkrétně Packet Data Channels ([PDCH](/mobilnisite/slovnik/pdch/)) a přidružené řídicí kanály – přidělovány, udržovány a uvolňovány v souvislosti s přechody stavů GMM a událostmi mobility.

V praxi jsou procedury GMMRR klíčové během událostí, jako je převýběr buňky a předání hovoru. Když UE provádí aktualizaci směrovací oblasti ([RAU](/mobilnisite/slovnik/rau/)) nebo změnu buňky, síť musí zajistit odpovídající přidělení rádiových prostředků v nové buňce. To zahrnuje účast BSS (Base Station Subsystem) v procesu mobility. Například během převýběru buňky mezi různými BSS může být nutná koordinace mezi zdrojovou a cílovou BSS pro přenos kontextu UE a opětovné navázání rádiových přenosových drah s minimálním přerušením služby. GMMRR to má optimalizovat definováním efektivních signalizačních a správních protokolů prostředků mezi BSS a SGSN.

Klíčovým aspektem GMMRR je manipulace s kontexty paketových toků a dočasnými blokovými toky (TBF). TBF je dočasné spojení navázané na rádiových prostředcích pro přenos dávky datových paketů. Procedury GMMRR zajišťují efektivní zřizování a rušení TBF při pohybu UE nebo při změně stavu její datové relace (např. při přechodu ze stavu ready do stavu standby). Tato optimalizace snižuje plýtvání rádiovými prostředky a zlepšuje celkovou kapacitu sítě a uživatelský zážitek. Specifikace podrobně popisují, jak BSS spravuje kontexty řízení rádiového spoje (RLC) v koordinaci se stavy GMM, což zajišťuje, že rádiové prostředky jsou drženy pouze tehdy, když jsou aktivně potřeba pro přenos dat, čímž se podporuje energeticky efektivní provoz UE a efektivní využití spektra sítí.

## K čemu slouží

GMMRR byl vyvinut k řešení specifických výzev spojených s integrací správy mobility s přepojováním paketů s omezenými prostředky rádiového rozhraní v GERAN. Rané implementace GPRS přistupovaly ke správě rádiových prostředků a správě mobility v jádru sítě poněkud nezávisle, což mohlo vést k neefektivitám. Například rádiové prostředky mohly být zbytečně drženy po události mobility nebo mohla být narušena kontinuita relace při změně buňky. Účelem GMMRR je těsně propojit tyto vrstvy pro optimalizovaný výkon.

Řeší problémy související s kontinuitou služby, efektivitou využití prostředků a signalizační zátěží během mobility v sítích 2.5G/3G. Koordinací procedur GMM s řízením rádiových prostředků na úrovni BSS umožňuje plynulejší předání hovoru a převýběr buňky pro paketové datové relace. To snižuje dobu přerušení dat a ztrátu paketů, čímž zlepšuje kvalitu uživatelského zážitku pro uživatele mobilních dat. Dále zajišťuje včasné uvolnění rádiových kanálů, když se UE stane nečinnou, čímž uvolňuje cenné spektrum pro jiné uživatele, což je klíčové pro kapacitně omezený rádiový přístup GSM/EDGE.

Jeho vznik byl motivován potřebou zlepšit výkon GPRS s rostoucím využíváním dat. Představuje optimalizaci v rámci vývoje GERAN, podrobně popsanou v technických specifikacích jako 43.901, pro zlepšení synergie mezi správou mobility v jádru sítě a přidělováním prostředků v rádiové síti, což připravilo cestu pro efektivnější nasazení EDGE a později EGPRS.

## Klíčové vlastnosti

- Koordinace přidělování rádiových prostředků s procedurami připojení/odpojení GPRS
- Optimalizovaná správa dočasných blokových toků (TBF) během mobility
- Efektivní přenos kontextu mezi BSS během předání hovoru mezi buňkami
- Uvolnění rádiových prostředků při přechodu UE do stavu idle/standby
- Integrace s procedurami Packet Flow Context (PFC) pro QoS
- Snížení přerušení služby během aktualizací směrovací oblasti

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)

## Definující specifikace

- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [GMMRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmmrr/)

---
slug: "pra"
url: "/mobilnisite/slovnik/pra/"
type: "slovnik"
title: "PRA – Presence Reporting Area"
date: 2026-01-01
abbr: "PRA"
fullName: "Presence Reporting Area"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pra/"
summary: "Přítomností hlášená oblast (PRA) je logická, konfigurovatelná geografická oblast definovaná v mobilní síti, která slouží ke sledování a hlášení přítomnosti nebo pohybu uživatelského zařízení (UE). Umo"
---

PRA je logická, konfigurovatelná geografická oblast v mobilní síti sloužící ke sledování a hlášení přítomnosti nebo pohybu uživatelského zařízení pro služby a optimalizace založené na poloze.

## Popis

Přítomností hlášená oblast (PRA) je síťově definovaná geografická zóna, konceptualizovaná ve standardech 3GPP, která poskytuje mechanismus pro hlášení polohy UE na úrovni podrobnosti mezi jedinou buňkou a velkou oblastí sledování ([TA](/mobilnisite/slovnik/ta/)). PRA může být vytvořena ze seznamu buněk, identifikátorů oblastí sledování ([TAI](/mobilnisite/slovnik/tai/)) nebo vysílačů ([eNB](/mobilnisite/slovnik/enb/)/gNB), nebo může být definována jako geografický tvar (např. polygon). Jedná se o logický konstrukt spravovaný jádrem sítě, konkrétně entitou správy mobility ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G, často ve spolupráci s funkcí pravidel pro účtování a politiky ([PCRF](/mobilnisite/slovnik/pcrf/)/[PCF](/mobilnisite/slovnik/pcf/)).

Jak to funguje, zahrnuje několik klíčových komponent a procedur. Nejprve je PRA zřízena v síti, čímž se definuje její identita (PRA ID), její součásti (buňky/TAI) a spouštěče hlášení (např. vstup UE do oblasti, opuštění oblasti nebo pobyt uvnitř oblasti). Tyto informace mohou být předány UE nebo použity pouze v rámci sítě. Když události mobility UE (jako změna buňky) odpovídají nakonfigurovaným spouštěčům pro monitorovanou PRA, rádiová přístupová síť (RAN) nebo samotné UE (v závislosti na konfiguraci) vygeneruje hlášení. Toto hlášení je odesláno do jádra sítě, které jej pak může předat externí aplikační funkci ([AF](/mobilnisite/slovnik/af/)) nebo jej použít interně pro optimalizaci sítě.

Z architektonického hlediska funkce PRA zasahuje do více síťových uzlů. PCRF/PCF může požadovat hlášení na základě PRA pro konkrétní UE jako součást řízení politiky a účtování, často iniciované služebním požadavkem AF. MME/AMF je zodpovědná za správu předplatného PRA pro UE, včetně aktivace, změny nebo deaktivace hlášení. Komunikuje relevantní informace o PRA k RAN (eNB/gNB) prostřednictvím signalizace S1/NGAP. RAN pak monitoruje polohu UE na úrovni buňky a podle toho spouští hlášení. V některých konfiguracích může být UE informováno o PRA a hlásit svou vlastní přítomnost, čímž se snižuje signalizační zátěž RAN.

Role PRA spočívá v poskytnutí flexibilního, efektivního nástroje pro služby citlivé na polohu. Například pro lokalizovanou vysílací službu (např. varování před zemětřesením) může AF požadovat upozornění, když UE vstoupí do PRA odpovídající postižené oblasti, a poté zahájit vysílání pouze v těchto buňkách. Pro optimalizaci mobility může síť definovat PRA kolem míst s přetížením a použít hlášení o vstupu ke spuštění akcí pro vyvažování zátěže. Nabízí cílenější alternativu k aktualizacím oblasti sledování (TAU), které pokrývají větší oblasti a jsou primárně určeny pro síťové vyvolané paging, nikoli pro aplikační služby založené na poloze.

## K čemu slouží

Přítomností hlášená oblast byla zavedena ve vydání 3GPP 12, aby řešila rostoucí poptávku po efektivních, síťově asistovaných službách polohy, které vyvažují přesnost s signalizační režií. Před PRA měly aplikace vyžadující znalost polohy UE omezené možnosti: mohly se spoléhat na nepřesné informace z oblasti sledování, zatěžovat síť častými, podrobnými požadavky na polohu (např. pomocí Cell-ID) nebo záviset výhradně na GNSS (GPS) UE, což spotřebovává baterii UE a nemusí být dostupné uvnitř budov.

Řeší problém poskytování aplikačně relevantních informací o poloze bez nadměrné signalizace v síti nebo spotřeby energie UE. PRA umožňuje síti definovat oblast zájmu jednou a poté přijímat automatická oznámení pouze při výskytu relevantních událostí mobility, namísto opakovaného dotazování na polohu UE. Tento model řízený událostmi je výrazně efektivnější pro služby, které potřebují vědět pouze tehdy, když UE překročí specifickou hranici, jako je geograficky vymezená reklama, lokalizované nouzové výstrahy nebo optimalizované ukládání obsahu na okraji sítě.

Její vytvoření bylo motivováno potřebou umožnit nové obchodní modely a techniky optimalizace sítě v éře LTE-Advanced a dále. Operátoři a poskytovatelé služeb hledali mechanismy pro nabízení služeb citlivých na kontext. PRA poskytuje standardizovaný způsob, jak tuto potřebu naplnit, usnadňuje hlášení polohy pro zákonné odposlechy, podporuje spouštěče polohy pro komunikaci typu stroj-stroj (MTC) a umožňuje funkcím jádra sítě, jako je funkce vystavení servisních schopností (SCEF/NEF), poskytovat polohu jako službu aplikacím třetích stran. Představuje posun k inteligentnějšímu, politikou řízenému řízení mobility.

## Klíčové vlastnosti

- Definuje logickou geografickou oblast složenou z buněk, TAI nebo eNB/gNB
- Podporuje konfigurovatelné spouštěče hlášení: vstup UE, výstup nebo přítomnost uvnitř oblasti
- Snižuje signalizační režii ve srovnání s nepřetržitým podrobným sledováním polohy
- Umožňuje síťové a aplikační služby a optimalizace založené na poloze
- Může být s asistencí UE nebo pouze síťové (založené na RAN) pro flexibilitu hlášení
- Integruje se s architekturou řízení politiky a účtování (PCC) pro požadavky iniciované AF

## Související pojmy

- [MMEC – Mobile Metaverse Enablement Client](/mobilnisite/slovnik/mmec/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 32.251** (Rel-19) — PS Domain Charging Management

---

📖 **Anglický originál a plná specifikace:** [PRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pra/)

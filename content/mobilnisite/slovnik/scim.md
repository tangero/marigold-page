---
slug: "scim"
url: "/mobilnisite/slovnik/scim/"
type: "slovnik"
title: "SCIM – Service Capability Interaction Manager"
date: 2025-01-01
abbr: "SCIM"
fullName: "Service Capability Interaction Manager"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scim/"
summary: "SCIM je logická funkce v architektuře IMS, která spravuje interakce mezi více aplikačními servery (AS) podílejícími se na obsluze jedné SIP relace. Koordinuje vyvolávání služeb, určuje pořadí jejich p"
---

SCIM je logická funkce IMS, která spravuje interakce a koordinuje provádění služeb mezi více aplikačními servery (AS) v rámci jedné SIP relace, aby zajistila konzistentní chování.

## Popis

Service Capability Interaction Manager (SCIM) je základní logická funkce definovaná v architektuře IP Multimedia Subsystem (IMS) podle 3GPP. Není to samostatný síťový prvek se specifickým protokolem, ale spíše funkční role, která může být implementována uvnitř [SIP](/mobilnisite/slovnik/sip/) aplikačního serveru ([AS](/mobilnisite/slovnik/as/)) nebo jako vyhrazená entita. Jejím hlavním úkolem je orchestrovat provádění více IMS služeb (např. přesměrování hovoru, presence, konferenční hovory), které jsou současně aplikovatelné na jednu SIP dialogovou relaci nebo registraci.

Z architektonického hlediska se SCIM nachází ve služební vrstvě IMS. Když [S-CSCF](/mobilnisite/slovnik/s-cscf/) na základě počátečních filtračních kritérií (iFCs) v profilu uživatele rozhodne o přesměrování SIP požadavku do služební vrstvy, může být tento požadavek směrován do uzlu implementujícího funkci SCIM. SCIM pak vystupuje jako zprostředkovatel. Obsahuje logiku pro určení, které konkrétní aplikační servery (AS) je třeba pro tuto relaci vyvolat, v jakém pořadí by měly být vyvolány a jak zpracovat tok SIP signalizace mezi nimi. SCIM přijme SIP požadavek, případně jej upraví a přepošle prvnímu AS. Poté přijme odpověď, rozhodne o dalším kroku a může přeposlat požadavek dalšímu AS podle logiky řetězení služeb.

Klíčovou technickou výzvou, kterou SCIM řeší, je správa interakcí služeb. Když jsou pro stejnou relaci spuštěny dvě nebo více služeb, mohou mezi nimi vznikat konflikty. Například služba přesměrování hovoru a služba zákazu hovoru mohou mít protichůdné záměry. Základní sekvenční vyvolání by mohlo vést k nesprávnému nebo nepředvídatelnému chování. SCIM obsahuje logiku pro správu interakcí, která může být založena na statických pravidlech priority, dynamické analýze za běhu nebo předdefinovaných maticích pro řešení konfliktů. Tato logika určuje konečný výsledek a zajišťuje, že služby interagují řízeným a deterministickým způsobem.

SCIM navíc může poskytovat přidané funkce, jako je kompozice služeb, kdy kombinuje schopnosti různých AS a vytváří tak pro uživatele nový, složený služební zážitek. Také chrání S-CSCF před složitostí správy interakcí více AS, což umožňuje S-CSCF udržovat jednodušší a standardizovanější rozhraní ke služební vrstvě. Implementace funkce SCIM je specifická pro dodavatele a její schopnosti se mohou pohybovat od jednoduchého sekvenčního přeposílání až po sofistikované orchestrace řízené politikami.

## K čemu slouží

SCIM byl koncipován k řešení kritického problému v paradigmatu poskytování služeb IMS: nekoordinovaného vyvolávání více, potenciálně nezávislých aplikačních serverů. V raných telefonních inteligentních sítích ([IN](/mobilnisite/slovnik/in/)) byla interakce služeb známou výzvou, ale často byla řešena v rámci jediného Service Control Point ([SCP](/mobilnisite/slovnik/scp/)). IMS se svým otevřeným, SIP-based a distribuovaným modelem [AS](/mobilnisite/slovnik/as/) riskoval vytvoření 'služebního chaosu', kde více AS, které si navzájem nejsou vědomy, mohlo zpracovat stejný [SIP](/mobilnisite/slovnik/sip/) požadavek konfliktními způsoby.

Bez SCIM by musel [S-CSCF](/mobilnisite/slovnik/s-cscf/) obsahovat složitou služební logiku pro správu sekvencí a konfliktů, což by porušovalo princip oddělení mezi základní vrstvou řízení relací a služební vrstvou. SCIM poskytuje pro tuto koordinaci vyhrazený architektonický bod. Jeho vytvoření bylo motivováno potřebou umožnit živé, více-dodavatelské ekosystémy IMS aplikací, kde by operátoři mohli nasazovat služby od různých poskytovatelů, aniž by riskovali selhání služeb kvůli nepředvídaným interakcím.

Řeší omezení lineárního řetězce vyvolávání založeného na filtračních kritériích zavedením inteligentního zprostředkovatele. To umožňuje vytváření sofistikovanějších, kombinovaných služeb a zajišťuje spolehlivé provádění služeb, což je nezbytné pro služby telekomunikační třídy carrier-grade. SCIM je klíčovým prvkem umožňujícím poskytování komplexních, personalizovaných komunikačních zážitků v síti IMS.

## Klíčové vlastnosti

- Orchestruje vyvolání více aplikačních serverů (AS) pro jednu SIP relaci
- Spravuje řetězení služeb a určuje pořadí jejich provádění
- Poskytuje logiku pro řešení konfliktů a interakcí mezi současně běžícími službami
- Vystupuje jako zprostředkovatel SIP signalizace mezi S-CSCF a více AS
- Umožňuje vytváření kompozitních služeb z více služebních schopností
- Chrání jádro IMS (S-CSCF) před složitostí služební vrstvy

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture

---

📖 **Anglický originál a plná specifikace:** [SCIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/scim/)

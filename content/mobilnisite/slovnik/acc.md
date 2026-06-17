---
slug: "acc"
url: "/mobilnisite/slovnik/acc/"
type: "slovnik"
title: "ACC – Automatic Congestion Control"
date: 2025-01-01
abbr: "ACC"
fullName: "Automatic Congestion Control"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acc/"
summary: "Mechanismus správy sítě, který automaticky detekuje a zmírňuje zahlcení v mobilních sítích. Monitoruje zatížení provozu a využití prostředků a následně uplatňuje předdefinované politiky ke snížení zah"
---

ACC je mechanismus správy sítě, který automaticky detekuje a zmírňuje zahlcení v mobilních sítích monitorováním zatížení provozu a uplatňováním politik pro udržení kvality a stability služeb.

## Popis

Automatic Congestion Control (ACC) je komplexní systém správy sítě definovaný ve standardech 3GPP, který umožňuje mobilním sítím autonomně detekovat, analyzovat a reagovat na stavy zahlcení. Systém funguje prostřednictvím nepřetržitého monitorování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)) napříč síťovými prvky včetně uzlů rádiového přístupu, brán jádra sítě a signalizačních rozhraní. Když jsou překročeny předdefinované prahové hodnoty zahlcení, ACC spouští automatizované akce pro zmírnění bez nutnosti manuálního zásahu operátorů sítě. Tento proaktivní přístup předchází situacím přetížení sítě, které by mohly vést k degradaci služeb, přerušeným hovorům nebo úplnému výpadku služeb.

Architektura ACC se skládá ze tří hlavních funkčních komponent: monitorovacích agentů rozmístěných po celé síti, centralizované funkce správy zahlcení a bodů vynucování politik. Monitorovací agenti sbírají data v reálném čase o využití prostředků, vzorcích provozu a metrikách výkonu. Tato data jsou agregována a analyzována funkcí správy zahlcení, která aplikuje algoritmy pro detekci vzorců zahlcení a predikci potenciálních situací přetížení. Na základě této analýzy systém vybírá vhodné strategie zmírnění z předdefinované databáze politik a instruuje body vynucování k implementaci těchto opatření.

ACC implementuje různé techniky zmírnění zahlcení v závislosti na postiženém segmentu sítě a typu zjištěného zahlcení. V rádiové přístupové síti to může zahrnovat úpravu parametrů řízení přístupu, modifikaci prahových hodnot pro předávání hovorů nebo dočasné snížení kvality služeb (QoS) pro určité třídy provozu. V jádru sítě může ACC implementovat tvarování provozu, omezení rychlosti nebo vyvažování zátěže napříč síťovými prvky. Systém využívá hierarchickou správu zahlcení, umožňující lokalizované reakce pro konkrétní síťové oblasti při zachování globální koordinace k zabránění šíření zahlcení.

Klíčové provozní aspekty zahrnují konfigurovatelné prahové hodnoty zahlcení, stupňované mechanismy odezvy a zpětnovazební smyčky pro vyhodnocení účinnosti zmírnění. ACC udržuje podrobné záznamy o událostech zahlcení a akcích zmírnění pro optimalizaci sítě a forenzní analýzu. Systém také podporuje různé provozní režimy, včetně preventivního předcházení zahlcení a reaktivního řešení zahlcení, což operátorům umožňuje vyvážit efektivitu sítě s cíli kvality služeb. Integrace s dalšími systémy správy sítě umožňuje koordinované reakce napříč více síťovými doménami.

## K čemu slouží

ACC byl vyvinut k řešení rostoucí výzvy síťového zahlcení v stále složitějších a intenzivně využívaných mobilních sítích. Před jeho zavedením se správa zahlcení silně spoléhala na manuální monitorování a zásahy týmů síťových operací, což bylo reaktivní, pomalé a často neúčinné během rychle se rozvíjejících situací zahlcení. Tento manuální přístup vedl k prodlouženým obdobím degradace služeb, nekonzistentní aplikaci opatření pro zmírnění zahlcení a zvýšeným provozním nákladům. Rozšíření datových služeb a exponenciální růst mobilního provozu vytvořily scénáře, kde se zahlcení mohlo vyvinout rychleji, než na něj mohli lidské operátory reagovat.

Primární motivací pro ACC bylo vytvořit automatizovaný, standardizovaný přístup ke správě zahlcení, který by mohl fungovat rychlostí sítě. Tradiční mechanismy řízení zahlcení byly často specifické pro dodavatele, omezeného rozsahu a postrádaly koordinaci napříč různými síťovými doménami. ACC poskytuje rámec pro holistickou správu zahlcení, který pokrývá prvky rádiového přístupu, přenosové sítě a jádra sítě. Tato standardizace umožňuje konzistentní implementaci napříč více-dodavatelskými sítěmi a usnadňuje interoperabilitu mezi systémy různých síťových operátorů.

ACC řeší několik kritických problémů v moderních mobilních sítích: zabraňuje ztrátě příjmů způsobené degradací služeb během událostí zahlcení, snižuje provozní náklady automatizací rutinních úloh správy zahlcení a zlepšuje spokojenost zákazníků udržováním dostupnosti služeb během období špičkového využití. Systém také řeší regulatorní požadavky na spolehlivost sítě a dostupnost služeb tísňového volání. Poskytováním předvídatelných, konzistentních reakcí na zahlcení umožňuje ACC síťovým operátorům optimalizovat využití prostředků při zachování smluv o úrovni služeb a kvality uživatelského zážitku pro koncové uživatele.

## Klíčové vlastnosti

- Detekce zahlcení v reálném čase prostřednictvím nepřetržitého monitorování KPI
- Automatizované zmírnění zahlcení založené na politikách bez manuálního zásahu
- Hierarchická správa zahlcení s lokalizovanou a globální koordinací
- Konfigurovatelné prahové hodnoty a stupňované mechanismy odezvy
- Integrace se stávajícími systémy správy sítě a řízení politik
- Podrobné zaznamenávání a reportování pro optimalizaci sítě a analýzu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [ACC na 3GPP Explorer](https://3gpp-explorer.com/glossary/acc/)

---
slug: "v-ees"
url: "/mobilnisite/slovnik/v-ees/"
type: "slovnik"
title: "V-EES – Visited Edge Enabler Server"
date: 2026-01-01
abbr: "V-EES"
fullName: "Visited Edge Enabler Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/v-ees/"
summary: "Síťová funkce v navštívené síti, která zprostředkovává služby edge computingu pro roamující uživatele. Slouží jako místní koncový bod služby, umožňuje aplikacím objevovat a využívat služby na okraji s"
---

V-EES (server pro povolení služeb na okraji sítě v navštívené síti) je funkce v navštívené síti, která zprostředkovává služby edge computingu pro roamující uživatele tím, že slouží jako místní koncový bod služby pro přístup s nízkou latencí.

## Popis

Visited Edge Enabler Server (V-EES) je funkční entita definovaná v rámci architektury 3GPP Edge Application Enablement (EAE) specifikované v TS 23.558. Nachází se v navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)) a slouží jako primární přístupový bod služby pro roamující uživatelské zařízení (UE), které chce využít prostředky edge computingu. Jejím hlavním úkolem je usnadňovat objevování, registraci a využívání aplikací a služeb na okraji sítě hostovaných v edge datových centrech navštívené sítě. V-EES komunikuje se serverem Home Edge Enabler Server ([H-EES](/mobilnisite/slovnik/h-ees/)) v domovské síti uživatele za účelem autorizace a ověření smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), čímž zajišťuje, že roamující uživatelé mohou bezproblémově přistupovat k povoleným edge službám.

Z architektonického hlediska V-EES poskytuje standardizované aplikační rozhraní ([API](/mobilnisite/slovnik/api/)) klientským aplikacím, známým jako Edge Enabler Clients ([EEC](/mobilnisite/slovnik/eec/)), které mohou být umístěny na UE nebo na aplikačním serveru. Když roamující UE požaduje edge službu, EEC komunikuje s V-EES. V-EES následně může dotazovat H-EES přes roamingové rozhraní EAE, aby ověřil uživatelský tarif a profil služeb. Po úspěšné autorizaci poskytne V-EES klientovi EEC potřebnou konfiguraci služby včetně adresy koncového bodu cílového Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)) umístěného v navštívené síti. Tento proces zajišťuje, že uživatelský provoz je směrován lokálně k optimálnímu edge uzlu, čímž se minimalizuje latence a zatížení přenosové sítě.

V-EES hraje klíčovou roli v kontinuitě a výkonu služeb v roamujících scénářích. Spravuje životní cyklus relací edge služeb, řeší potenciální opětovné objevování služeb v důsledku mobility UE a může shromažďovat údaje o využití pro účely účtování. Oddělením autorizace služeb (kterou zajišťuje H-EES) od místního poskytování služeb (které zajišťuje V-EES) architektura podporuje jak model služeb směrovaných přes domovskou síť, tak model místního průniku pro edge computing. Její implementace je klíčová pro dosažení globálně konzistentního uživatelského zážitku s nízkou latencí pro mobilní uživatele přistupující k náročným aplikacím, jako je rozšířená realita, průmyslová automatizace nebo služby propojených vozidel, když se nacházejí mimo pokrytí své domovské sítě.

## K čemu slouží

V-EES byl zaveden, aby vyřešil problém poskytování efektivních služeb edge computingu s nízkou latencí roamujícím uživatelům. Před jeho standardizací byly edge služby navrženy primárně pro uživatele v jejich domovské síti. Roamující uživatelé buď nemohli přistupovat k místním edge prostředkům, nebo byl jejich provoz nuceně směrován zpět do domovské sítě, což způsobovalo vysokou latenci a zahlcení spojů jádra sítě, což popírá hlavní výhodu edge computingu. To byla významná překážka pro aplikace citlivé na latenci, jako je autonomní řízení, hraní her v reálném čase a rozšířená realita ([XR](/mobilnisite/slovnik/xr/)), které vyžadují konzistentní výkon bez ohledu na polohu uživatele.

Vytvoření V-EES jako součásti širší architektury EAE ve verzi Release 18 bylo motivováno komerční potřebou operátorů nabízet pokročilé edge služby v globálním měřítku. Umožňuje operátorům navštívené sítě zpřístupnit a zpeněžit svou edge infrastrukturu roamujícím účastníkům od partnerských operátorů. Technicky řeší problém objevování služeb a řízení přístupu v prostředí více operátorů. Bez standardizované entity na straně navštívené sítě, jako je V-EES, by každá dvojice operátorů potřebovala vlastní integrace, což by bránilo škálovatelnosti. V-EES poskytuje potřebný kotvící bod v navštívené síti pro ověření roamujících požadavků (prostřednictvím domovské sítě), objevení místních instancí edge aplikací a zajištění dodání služeb v souladu s politikami domovského operátora uživatele.

## Klíčové vlastnosti

- Místní objevování edge služeb pro roamující UE
- Propojení s domovským EES (H-EES) pro autorizaci a politiky
- Poskytování standardizovaných EAE API klientům Edge Enabler Clients
- Podpora jak klientů služeb na straně UE, tak na straně aplikace
- Správa životního cyklu relací edge aplikací v navštívené síti
- Shromažďování údajů o využití pro účtování a vyúčtování mezi operátory

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [V-EES na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-ees/)

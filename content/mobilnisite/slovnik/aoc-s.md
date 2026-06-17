---
slug: "aoc-s"
url: "/mobilnisite/slovnik/aoc-s/"
type: "slovnik"
title: "AOC-S – Advice Of Charge at communication Set-up time"
date: 2026-01-01
abbr: "AOC-S"
fullName: "Advice Of Charge at communication Set-up time"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc-s/"
summary: "AOC-S je služba účtování podle 3GPP, která uživatelům poskytuje informace o nákladech při zřízení hovoru nebo relace. Umožňuje účastníkům obdržet odhadované podrobnosti o ceně před přijetím poplatku z"
---

AOC-S je služba účtování podle 3GPP, která účastníkům poskytuje informace o odhadovaných nákladech při zřízení hovoru nebo relace, aby umožnila transparentní fakturaci a kontrolu nákladů.

## Popis

Advice Of Charge at communication Set-up time (AOC-S) je standardizovaná doplňková služba v architektuře 3GPP, která doručuje informace o ceně uživatelům při zahájení komunikační relace. Služba funguje v rámci IP Multimedia Subsystem (IMS) a využívá stávající architekturu účtování k výpočtu a prezentaci odhadu nákladů předtím, než se uživatel zaváže k hovoru nebo relaci. AOC-S se integruje s online i offline systémy účtování ([OCS](/mobilnisite/slovnik/ocs/) a [OFCS](/mobilnisite/slovnik/ofcs/)) za účelem získání tarifních informací a generování přesných cenových předpovědí na základě cíle, typu služby a tarifního plánu účastníka.

Z architektonického hlediska je funkčnost AOC-S implementována napříč více síťovými elementy. Serving-Call Session Control Function (S-CSCF) hraje klíčovou roli při vyvolání AOC-S během procedur zřizování relace. Když uživatel zahájí hovor nebo relaci, která spouští AOC-S, S-CSCF komunikuje s Online Charging System (OCS) přes rozhraní Ro, aby získal informace o ceně v reálném čase. OCS vypočítá odhadovanou cenu na základě profilu účastníka, cílové sítě, charakteristik služby a aplikovatelných tarifů. Tyto informace jsou následně naformátovány a doručeny do uživatelského zařízení prostřednictvím signalizačních zpráv SIP.

Služba podporuje více mechanismů doručení v závislosti na schopnostech uživatelského zařízení a konfiguraci sítě. U schopných zařízení mohou být informace AOC-S zobrazeny vizuálně na obrazovce, prezentovány zvukově prostřednictvím hlášení nebo doručeny pomocí SMS. Informace o ceně typicky zahrnují odhadovanou cenu za časovou jednotku (minutu/vteřinu), cenu za datovou jednotku (megabajt) nebo paušální poplatky za konkrétní službu. AOC-S také zvládá různé scénáře včetně tuzemských hovorů, mezinárodních hovorů, situací roamingu a speciálních služebních čísel, kde se tarify mohou výrazně lišit od standardních sazeb.

Klíčové komponenty zapojené do implementace AOC-S zahrnují User Equipment (UE) s podporou AOC-S, S-CSCF pro spouštění a řízení služby, OCS pro výpočty ceny v reálném čase a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro ukládání profilů služeb účastníka. Služba komunikuje s referenčním bodem Ro založeným na protokolu Diameter mezi S-CSCF a OCS za účelem výměny informací o ceně. AOC-S se také integruje s rozhraním Ut pro konfiguraci uživatele, což umožňuje účastníkům službu povolit nebo zakázat prostřednictvím webových správcovských rozhraní.

Při provozu AOC-S následuje konkrétní sekvenci: když uživatel zahájí hovor, S-CSCF detekuje na základě profilu v HSS, že je AOC-S pro tohoto účastníka aktivní. S-CSCF následně pozastaví zřizování relace a dotazuje se OCS na informace o ceně. OCS odpoví s příslušnými tarifními podrobnostmi, které S-CSCF začlení do signalizace SIP. Uživatelské zařízení tyto informace přijme a prezentuje je uživateli, který se pak může na základě cenového odhadu rozhodnout, zda v hovoru pokračovat. Celý tento proces proběhne během milisekund, aby bylo minimalizováno zpoždění při zřizování hovoru, a zároveň poskytl cennou transparentnost v účtování.

## K čemu slouží

AOC-S byl vyvinut, aby řešil kritickou potřebu transparentnosti účtování v mobilní telekomunikaci, zejména když se služby stávaly složitějšími a mezinárodní roaming se rozšiřoval. Před implementací AOC-S často účastníci dostávali neočekávané poplatky za hovory, obzvláště při roamingu nebo při používání prémiových služeb, což vedlo k šoku z výše účtu a nespokojenosti zákazníků. Služba byla vytvořena, aby uživatelům poskytla předem informace o nákladech a umožnila jim tak informovaně se rozhodnout, zda v komunikaci pokračovat na základě jejich rozpočtu a znalosti tarifů.

Historický kontext vývoje AOC-S vychází z rostoucí složitosti struktur mobilního účtování v sítích 3GPP. Jak operátoři zaváděli různé tarifní plány, mezinárodní roamingové dohody a nabídky prémiových služeb, účastníkům bylo obtížné přesně předpovídat náklady na komunikaci. Tradiční přístupy spoléhaly na fakturační výpisy po hovoru nebo vyžadovaly, aby si uživatelé tarify ručně ověřovali prostřednictvím samostatných kanálů. AOC-S tyto nedostatky řešil integrací informací o ceně přímo do procesu zřizování hovoru, čímž poskytoval odhady nákladů v reálném čase a s ohledem na kontext, aniž by vyžadoval další akce uživatele.

AOC-S také řešil konkrétní problémy související s regulatorními požadavky na různých trzích, kde zákony na ochranu spotřebitele vyžadovaly transparentní cenové informace. Standardizací této funkčnosti v rámci specifikací 3GPP mohli operátoři implementovat konzistentní transparentnost účtování napříč různými sítěmi a zařízeními. Služba byla obzvláště přínosná pro firemní uživatele, kteří potřebovali kontrolovat náklady na komunikaci, a pro účastníky cestující do zahraničí, kteří čelili nepředvídatelným roamingovým poplatkům. AOC-S představoval významný krok k uživatelsky orientovaným systémům účtování, které upřednostňují transparentnost a kontrolu před následným vysvětlováním fakturace.

## Klíčové vlastnosti

- Doručování informací o ceně v reálném čase při zřizování relace
- Integrace s Online Charging System (OCS) přes rozhraní Ro
- Podpora více formátů prezentace (vizuální, zvuková, SMS)
- Podpora scénářů roamingu s koordinací účtování ve visited síti
- Uživatelsky konfigurovatelná aktivace přes rozhraní Ut
- Výpočet tarifu na základě cíle, typu služby a profilu účastníka

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions

---

📖 **Anglický originál a plná specifikace:** [AOC-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc-s/)

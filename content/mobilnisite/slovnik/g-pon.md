---
slug: "g-pon"
url: "/mobilnisite/slovnik/g-pon/"
type: "slovnik"
title: "G-PON – Gigabit Passive Optical Network"
date: 2025-01-01
abbr: "G-PON"
fullName: "Gigabit Passive Optical Network"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/g-pon/"
summary: "Optická přístupová síťová technologie standardizovaná ITU-T, na kterou odkazují specifikace 3GPP v kontextu integrace pevných sítí. Poskytuje vysokou přenosovou kapacitu a spojení typu bod–více bodů s"
---

G-PON je optická přístupová síťová technologie, standardizovaná ITU-T a odkazovaná v 3GPP, která poskytuje vysokorychlostní spojení typu bod–více bodů pro nákladově efektivní služby FTTH a je studována jako důvěryhodný přístup mimo 3GPP pro konvergenci 5G.

## Popis

Gigabit Passive Optical Network (G-PON) je přístupová síťová technologie definovaná standardy [ITU-T](/mobilnisite/slovnik/itu-t/) řady G.984. Ačkoli se nejedná o rádiovou technologii definovanou 3GPP, je v rámci specifikací 3GPP odkazována, zejména v kontextu integrace pevných sítí a konvergence systému 5G. Systém G-PON je optická síťová architektura typu bod–více bodů, která se skládá z optické linkové terminace (OLT) v centrální ústředně poskytovatele služeb, pasivního optického rozdělovače a více optických síťových jednotek (ONU) nebo optických síťových terminálů (ONT) u zákazníka. „Pasivní“ povaha odkazuje na využití neaktivních (nevyžadujících napájení) optických rozdělovačů v distribuční síti, což ve srovnání s aktivními elektronickými uzly snižuje spotřebu energie a náklady na údržbu.

Architektura funguje pomocí různých vlnových délek pro vysílání downstream (z OLT k ONU) a upstream (z ONU k OLT), což umožňuje plně duplexní komunikaci po jediném vlákně. Downstream provoz je vysílán OLT všem ONU připojeným ke stejnému rozdělovači; každá ONU filtruje a přijímá pouze pakety adresované jí. Upstream přenos je složitější, protože více ONU sdílí stejný upstreamový kanál. Aby se předešlo kolizím, OLT řídí upstreamový přístup pomocí schématu vícečetného přístupu s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)). OLT přiděluje každé ONU konkrétní časové sloty, během nichž může daná ONU vysílat své datové přenosy. Tato dynamická alokace šířky pásma (DBA) je klíčovou vlastností, která umožňuje OLT efektivně rozdělovat upstreamovou kapacitu na základě reálných požadavků každého účastníka.

V kontextu 3GPP je G-PON považován za typ důvěryhodné přístupové sítě mimo 3GPP. To znamená, že síť jádra 5G (5GC) může autentizovat a integrovat koncové zařízení připojené přes G-PON spojení a zacházet s ním podobně jako s přístupem přes 3GPP rádiové rozhraní. Pro tuto integraci může ONU/ONT obsahovat funkci autentizace přístupu k síti definovanou 3GPP, nebo může směrovač uživatele za ONT navázat tunel [IPsec](/mobilnisite/slovnik/ipsec/) s funkcí pro propojení s přístupy mimo 3GPP ([N3IWF](/mobilnisite/slovnik/n3iwf/)) v 5GC. Studium této integrace je pokryto v dokumentu 3GPP TR 22.906. Úlohou G-PON je poskytnout ultrarychlý pevný přístup s nízkou latencí, který lze kombinovat s mobilitou 5G, a podporovat tak případy užití jako konvergence pevného bezdrátového přístupu ([FWA](/mobilnisite/slovnik/fwa/)), síťové dělení pro rezidenční broadband a plynulou kontinuitu služeb mezi pevnými a mobilními sítěmi.

## K čemu slouží

Technologie G-PON byla vyvinuta k uspokojení rostoucí poptávky po vysokorychlostním přístupu k internetu pro domácnosti a firmy, známého jako přivedení optiky do domácnosti (FTTH) nebo do objektu (FTTP). Jejím cílem je poskytnout nákladově efektivní a budoucím potřebám vyhovující alternativu k přístupovým technologiím na bázi měděných vedení, jako je [DSL](/mobilnisite/slovnik/dsl/) nebo kabelové modemy, které mají omezenou přenosovou kapacitu a dosah. Pasivní návrh významně snižuje provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) tím, že odstraňuje aktivní elektroniku v terénu, která vyžaduje napájení a klimatizované prostředí. To činí nasazení optiky ekonomičtějším, zejména v oblastech s nízkou hustotou účastníků.

Zájem 3GPP o G-PON a odkazování na něj vychází ze strategického cíle konvergence sítí a případu užití „konvergence pevných a mobilních sítí v 5G“. Jak se standardy 5G vyvíjely, bylo uznáno, že ne všechna přístupová řešení budou bezdrátová; vysokovýkonné pevné přístupové sítě jako G-PON (a jeho nástupce XGS-PON) jsou klíčovými komponentami holistické širokopásmové strategie. Definováním architektur pro integraci důvěryhodných přístupů mimo 3GPP, jako je G-PON, umožňuje 3GPP operátorům nabízet jednotné služby a politiky napříč mobilní i pevnou doménou. Účastník by například mohl mít jediné předplacené služby nabízející plynulý provoz doma přes G-PON a na cestách přes 5G NR.

Tato integrace řeší problém izolovaných sítí. Před takovou konvergencí byly pevné a mobilní sítě provozovány a spravovány nezávisle, což vedlo ke zdvojování funkcí, odděleným databázím účastníků a roztříštěné uživatelské zkušenosti. Odkazování na G-PON v rámci architektury 3GPP umožňuje standardizovanou autentizaci, řízení politik a účtování (prostřednictvím 5GC) pro uživatele na kterémkoli typu přístupu. Motivuje to k vytvoření skutečně jednotného síťového jádra, které dokáže agregovat provoz z různých přístupových technologií, zjednodušit provoz a umožnit inovativní balíčkové služby.

## Klíčové vlastnosti

- Topologie typu bod–více bodů využívající pasivní optické rozdělovače, což snižuje množství aktivní elektroniky v terénu
- Vysoká přenosová kapacita, typicky 2,5 Gbps downstream a 1,25 Gbps upstream na vlnovou délku
- Dynamická alokace šířky pásma (DBA) pro efektivní plánování upstreamového TDMA
- Velký dosah (až 20 km) a vysoký poměr dělení (např. 1:64 nebo 1:128)
- Podpora služeb triple-play (data, hlas, video) po jediném vlákně
- Odkazováno v 3GPP jako důvěryhodný typ přístupu mimo 3GPP pro konvergenci sítí 5G

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TR 22.906** (Rel-19) — IMS P2P Content Distribution Services

---

📖 **Anglický originál a plná specifikace:** [G-PON na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-pon/)

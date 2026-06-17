---
slug: "megc"
url: "/mobilnisite/slovnik/megc/"
type: "slovnik"
title: "MEGC – MCPTT Emergency Group Call"
date: 2025-01-01
abbr: "MEGC"
fullName: "MCPTT Emergency Group Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/megc/"
summary: "Specifický typ služby nouzového volání v rámci MCPTT, který je směrován na předdefinovanou nouzovou skupinu MCPTT (MEG). Poskytuje nejvyšší prioritu, zajišťuje okamžité sestavení, preventivní alokaci"
---

MEGC (MCPTT hovor pro nouzovou skupinu) je služba MCPTT nouzového volání s vysokou prioritou směrovaná na předdefinovanou skupinu, zajišťující okamžité sestavení a spolehlivou komunikaci pro situace kritické z hlediska životů.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Emergency Group Call (MEGC) je vlastní procedura vyvolání služby a sestavení relace, která využívá nouzovou skupinu MCPTT ([MEG](/mobilnisite/slovnik/meg/)). Představuje komplexní proces od začátku do konce pro zahájení, autorizaci, sestavení a udržování skupinové komunikační relace v reálném čase (obvykle poloduplexní hlasové), cílené na konkrétní MEG. Tato služba je klíčovou součástí sady 3GPP Mission Critical Services. Z architektonického hlediska se na ní podílí MCPTT klient na zařízení uživatele, aplikační server MCPTT a podpůrné přístupové a jádrové sítě 3GPP ([E-UTRAN](/mobilnisite/slovnik/e-utran/)/EPC nebo NG-RAN/5GC).

Pracovní postup začíná, když autorizovaný uživatel MCPTT aktivuje funkci nouzového skupinového hovoru a určí identifikátor cílové MEG. MCPTT klient odešle požadavek na službu aplikačnímu serveru MCPTT přes navázané signalizační spojení (pomocí protokolů jako je SIP přes IMS). Tento požadavek je označen jako nouzový. Server MCPTT provede několik klíčových kontrol: autentizuje uživatele, ověří jeho autorizaci zahájit hovor k požadované MEG a načte aktuální seznam členů této MEG. Po ověření server zahájí sestavení mediální relace. Klíčovým rozlišovacím znakem MEGC je její interakce s rámcem pro řízení politiky a účtování (PCC) sítě. Server MCPTT komunikuje s funkcí pro řízení politiky ([PCF](/mobilnisite/slovnik/pcf/)), aby požádal o zřízení vyhrazeného, prioritního přenosového kanálu (bearer) (ve 4G) nebo QoS toku (v 5G) pro mediální stream. Tento kanál je přiřazen identifikátor třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) nebo [5QI](/mobilnisite/slovnik/5qi/) s vysokou prioritou, často s možností přednostního přerušení jiných přenosů, aby bylo zajištěno, že hovor nebude blokován přetížením sítě.

Současně server signalizuje všem MCPTT klientům členů MEG (kromě iniciátora), aby je upozornil na příchozí nouzový skupinový hovor. Tato upozornění jsou typicky intruzivní a mohou přerušit jiné činnosti zařízení. Jakmile je mediální cesta sestavena přes funkce uživatelské roviny sítě ([UPF](/mobilnisite/slovnik/upf/) v 5G, PGW v 4G), vytvoří se distribuční strom médií typu jeden k mnoha, kde je zvukový stream iniciátora replikován všem členům skupiny. Server spravuje řízení práva mluvit (floor control) pro hovor, přiděluje právo mluvit podle pravidel MCPTT, což u nouzových hovorů může zahrnovat přednostní přidělení práva. Hovor trvá, dokud není explicitně ukončen, a poskytuje stabilní kanál pro koordinaci při krizi.

## K čemu slouží

MEGC byl vytvořen, aby splnil přísný požadavek na okamžitou, garantovanou a celoskupinovou komunikaci během operací veřejné bezpečnosti a zásahových týmů. Zatímco obecné skupinové hovory [MCPTT](/mobilnisite/slovnik/mcptt/) poskytují efektivní týmovou komunikaci, nemusí mít absolutní prioritu a garance zdrojů vyžadované pro situace ohrožující život. MEGC tuto mezeru zaplňuje definováním specializované třídy služeb s nejvyšší prioritou v rámci MCPTT. Problém, který řeší, je potenciální selhání nebo zpoždění kritického skupinového hovoru kvůli přetížení sítě, soupeření s jinými službami nebo složitým procedurám sestavení.

Historicky používaly zásahové týmy push-to-talk v systémech LMR, kde nouzový skupinový hovor často znamenal přepnutí na vyhrazený, předem alokovaný "nouzový" kanál nebo použití funkce zabrání kanálu. Účelem standardizace MEGC v 3GPP (počínaje Release 13) bylo replikovat a vylepšit tuto schopnost v širokopásmových sítích LTE a 5G. Řeší omezení komunikace IP typu best-effort tím, že ukládá síti povinnost vynucovat prioritu od konce ke konci, od rádiového rozhraní přes jádro sítě až k aplikačnímu serveru. To zajišťuje, že nouzová komunikace od autorizovaného personálu může přerušit jiný síťový provoz, což je klíčová schopnost během velkých incidentů, kdy se veřejné sítě přetíží. Jeho vytvoření bylo motivováno potřebou standardizované, interoperabilní a na úrovni operátora (carrier-grade) funkce nouzového skupinového hovoru, kterou lze globálně nasadit na komerčních sítích, což umožní bezproblémovou spolupráci mezi různými agenturami a přes geografické hranice.

## Klíčové vlastnosti

- Vyvolání cílené na konkrétní předdefinovanou nouzovou skupinu MCPTT (MEG)
- Priorita a možnost přednostního přerušení v celé síti (vysoká priorita QCI/5QI)
- Intruzivní upozornění a automatické přijetí pro volané členy skupiny
- Integrované s řízením práva mluvit (floor control) MCPTT, případně s nouzovou prioritou
- Zabezpečená autorizace a ověření iniciátora i skupiny
- Podpora pro provoz v síti i mimo síť (pomocí ProSe)

## Související pojmy

- [MEG – MCPTT Emergency Group](/mobilnisite/slovnik/meg/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MEGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/megc/)

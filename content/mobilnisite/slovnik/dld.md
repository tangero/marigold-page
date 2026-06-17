---
slug: "dld"
url: "/mobilnisite/slovnik/dld/"
type: "slovnik"
title: "DLD – Data Link Discriminator"
date: 2025-01-01
abbr: "DLD"
fullName: "Data Link Discriminator"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dld/"
summary: "Parametr používaný v některých signalizačních protokolech 3GPP core sítě k rozlišení různých spojení datového spoje nebo signalizačních asociací, zejména v kontextu Base Station System Application Par"
---

DLD je parametr používaný v signalizaci 3GPP core sítě, například v BSSAP, k rozlišení různých spojení datového spoje pro správné směrování zpráv v rámci síťového uzlu.

## Popis

Data Link Discriminator (DLD) je specifický identifikátor používaný v rámci signalizační architektury 3GPP core sítě, zejména ve spojení se sadou protokolů Base Station System Application Part ([BSSAP](/mobilnisite/slovnik/bssap/)). BSSAP usnadňuje komunikaci mezi Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Base Station System ([BSS](/mobilnisite/slovnik/bss/)) v sítích GSM. Úlohou DLD je rozlišovat mezi různými signalizačními spojeními nebo datovými spoji, které mohou existovat mezi stejnými dvěma síťovými entitami (např. MSC a [BSC](/mobilnisite/slovnik/bsc/)). Funguje jako lokální identifikátor na úrovni uživatele SCCP (Signaling Connection Control Part) pro asociaci příchozích BSSAP zpráv s konkrétním dialogem nebo transakčním kontextem.

V praktickém provozu, když je mezi MSC a BSS navázáno SCCP spojení pro specifický účel (jako je nastavení hovoru ukončeného mobilním účastníkem), začíná BSSAP dialog. Tomuto dialogu je přiřazena hodnota DLD. Všechny BSSAP zprávy patřící k tomuto konkrétnímu dialogu nebo procedurální instanci budou nést stejnou hodnotu DLD ve svém poli rozlišovače protokolu nebo v rámci struktury zprávy. Když MSC nebo BSS přijme BSSAP zprávu, použije DLD ve spojení s dalšími identifikátory, jako je Circuit Identity Code ([CIC](/mobilnisite/slovnik/cic/)) pro hovory vázané na okruh, k nalezení správného interního stavového automatu nebo instance hovoru, ke kterému se zpráva vztahuje.

Z architektonického hlediska DLD pracuje na aplikační vrstvě (vrstva 7), ale plní spojovací funkci k podkladové transportní službě poskytované SCCP. Je obzvláště důležitý pro správu více paralelních transakcí, jako je zpracování několika současných nastavení hovorů nebo předání spojení pro různé účastníky přes stejný signalizační link. Zajišťuje, že zprávy nejsou zpracovány v nesprávném kontextu, což by mohlo vést k přerušení hovoru nebo nesprávným akcím správy mobility. Specifikace, jako je TS 49.008 (BSSAP), podrobně popisují, jak je DLD spravován a používán v rámci sekvencí zpráv.

## K čemu slouží

Data Link Discriminator byl zaveden k vyřešení nejednoznačnosti v směrování zpráv v rámci signalizační roviny core sítě, zejména když mezi stejnými dvěma síťovými uzly probíhá současně více nezávislých signalizačních dialogů nebo transakcí přes stejný signalizační link. Bez tohoto rozlišovače by [MSC](/mobilnisite/slovnik/msc/) přijímající [BSSAP](/mobilnisite/slovnik/bssap/) zprávu související s předáním spojení nemělo spolehlivý způsob, jak ji asociovat se správným probíhajícím hovorem z několika možných, pokud sdílejí stejné obecné adresování.

Jeho vznik byl motivován potřebou robustní stavové signalizace v GSM. Protokoly jako BSSAP řídí komplexní procedury (např. předání spojení, šifrování, přiřazení), které zahrnují sekvenci zpráv. Každá procedura má svůj vlastní kontext. DLD poskytuje jednoduchý a efektivní způsob, jak vázat každou zprávu na její specifický kontext na aplikační vrstvě, a doplňuje tak službu s navázáním spojení poskytovanou SCCP na transportní vrstvě.

Řeší omezení použití pouze adres nižších vrstev (jako jsou ID spojení SCCP nebo identifikátory okruhů), které nemusí být dostatečně podrobné nebo nemusí existovat pro všechny typy signalizačních interakcí. DLD zajišťuje, že i signalizace nevázaná na okruh (např. pro správu mobility) nebo více signálů vázaných na okruh pro různé zdroje mohou být jasně rozlišeny, čímž se zabrání vzájemnému ovlivňování nezávislých síťových procedur a zvýší se celková spolehlivost signalizace a stabilita sítě.

## Klíčové vlastnosti

- Používá se v rámci BSSAP a souvisejících protokolů k rozlišení různých signalizačních dialogů nebo procedurálních instancí.
- Funguje jako lokální identifikátor kontextu pro směrování zpráv aplikační vrstvy ke správnému internímu stavovému automatu.
- Nezbytný pro správu více souběžných transakcí (např. hovorů, předání spojení) mezi MSC a BSS.
- Obsažen v poli rozlišovače protokolu nebo ve struktuře zpráv BSSAP.
- Pracuje ve spojení s dalšími identifikátory, jako je Circuit Identity Code (CIC), pro komplexní identifikaci kontextu.
- Podrobně popsán v signalizačních specifikacích core sítě, jako je TS 49.008.

## Související pojmy

- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)
- [CIC – Call Identifier Code / Circuit Identifier Code](/mobilnisite/slovnik/cic/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [DLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dld/)

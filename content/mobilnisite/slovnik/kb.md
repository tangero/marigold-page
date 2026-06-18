---
slug: "kb"
url: "/mobilnisite/slovnik/kb/"
type: "slovnik"
title: "KB – Kilo Byte"
date: 2025-01-01
abbr: "KB"
fullName: "Kilo Byte"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kb/"
summary: "Standardní jednotka digitální informace nebo datového úložiště rovná 1000 bytům (v desítkové soustavě SI) nebo 1024 bytům (v binární soustavě). Je všudypřítomně používána v 3GPP specifikacích pro kvan"
---

KB je standardní jednotka digitální informace rovná 1000 nebo 1024 bytům, která je v 3GPP specifikacích všudypřítomně používána pro kvantifikaci objemu dat, velikosti zpráv, propustnosti a požadavků na úložiště.

## Popis

V technických specifikacích 3GPP je KB (Kilo Byte) základní měrnou jednotkou objemu dat. Její přesný význam závisí na kontextu a odpovídá běžné výpočetní praxi: může představovat 1000 bytů (10^3 bytů) podle Mezinárodní soustavy jednotek ([SI](/mobilnisite/slovnik/si/)) nebo 1024 bytů (2^10 bytů) podle binární interpretace běžné v informatice. Specifikace 3GPP často upřesňují použití v normativních kontextech, zejména při definování prahových hodnot, limitů nebo požadavků na výkon. Například specifikace může stanovit maximální velikost zprávy jako „64 KB“ s poznámkou definující ji jako 65536 bytů (64 * 1024).

Jeho použití je všudypřítomné napříč všemi vrstvami architektury. Na fyzické vrstvě a v řízení rádiových zdrojů se KB používá k popisu velikostí transportních bloků, hlášení stavu vyrovnávací paměti a objemů dat pro plánování. V jádru sítě a při návrhu protokolů kvantifikuje velikosti paketových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)), záznamy o účtovaných datech ([CDR](/mobilnisite/slovnik/cdr/)), užitečná zatížení signalizačních zpráv a prahové hodnoty pro řízení politik (jako jsou limity datového využití). Ve specifikacích služeb a aplikační vrstvy definuje data kodeků, užitečná zatížení aplikačních serverů a požadavky na paměť UE.

Z provozní perspektivy se výkon síťového zařízení často měří v KB za sekundu (KBps) pro propustnost nebo v KB pro kapacitu paměti. Tato jednotka je nedílnou součástí definování parametrů kvality služby (QoS), zejména pro hodnoty garantované přenosové rychlosti ([GBR](/mobilnisite/slovnik/gbr/)) a maximální přenosové rychlosti ([MBR](/mobilnisite/slovnik/mbr/)), které mohou být vyjádřeny v kilobitech za sekundu (kbps), ale jsou odvozeny od manipulace s daty na úrovni bytů. Pochopení měřítka, které KB implikuje, je nezbytné pro inženýry navrhující rozhraní, dimenzující síťovou kapacitu, implementující vyrovnávací paměti a zajišťující soulad s omezeními velikosti protokolových dat specifikovanými v tisících technických dokumentů 3GPP.

## K čemu slouží

Použití KB jako standardní jednotky slouží základnímu účelu poskytování konzistentní, škálovatelné metriky pro kvantifikaci digitální informace napříč rozsáhlým a komplexním ekosystémem definovaným 3GPP. Bez takové standardizované jednotky by byly specifikace nejednoznačné, což by vedlo k problémům s interoperabilitou mezi zařízeními od různých dodavatelů. Řeší problém vyjadřování množství dat čitelným a technicky přesným způsobem, což překlenuje propast mezi popisy služeb na vysoké úrovni a implementačními detaily na nízké úrovni.

Historicky, jak se buněčné systémy vyvíjely od sítí zaměřených na hlas (2G) k sítím zaměřeným na data (3G/4G/5G), stala se potřeba přesně specifikovat množství dat kritickou. Rané specifikace mohly odkazovat na menší jednotky, ale exploze mobilních dat si vyžádala praktickou jednotku pro každodenní použití – KB, MB, GB. Její přijetí bylo motivováno potřebou definovat tarify (např. datové balíčky), výkonnostní metriky (např. propustnost) a technické limity (např. maximální velikost [PDU](/mobilnisite/slovnik/pdu/)) jasným, všeobecně srozumitelným formátem.

Řeší omezení nejednoznačných nebo nestandardních měření. Použitím KB zajišťuje 3GPP, že když norma vyžaduje schopnost UE zpracovat zprávu určité velikosti nebo síť podporovat určitou datovou rychlost, mají všichni implementátoři společný referenční bod. Tato jednotnost je klíčová pro globální interoperabilitu, testování, certifikaci a v konečném důsledku pro poskytování konzistentního uživatelského zážitku bez ohledu na základní hardwarovou nebo softwarovou implementaci síťových prvků.

## Klíčové vlastnosti

- Standardizovaná jednotka pro měření objemu dat (1000 nebo 1024 bytů) v 3GPP specifikacích.
- Všudypřítomně používána napříč fyzickou, protokolovou a služební vrstvou pro definice velikostí a kapacit.
- Nezbytná pro definování parametrů QoS, velikostí vyrovnávacích pamětí a limitů užitečného zatížení zpráv.
- Poskytuje společný referenční bod pro testování interoperability a certifikaci zařízení.
- Škálovatelná na větší jednotky (MB, GB) pro popis datových tarifů a úložiště.
- Základ pro výpočet datových rychlostí (např. KBps) a metrik výkonu propustnosti.

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [KB na 3GPP Explorer](https://3gpp-explorer.com/glossary/kb/)

---
slug: "lscs"
url: "/mobilnisite/slovnik/lscs/"
type: "slovnik"
title: "LSCS – Local Supported Codec Set"
date: 2025-01-01
abbr: "LSCS"
fullName: "Local Supported Codec Set"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lscs/"
summary: "Seznam hlasových a multimediálních kodeků, které uživatelské zařízení (UE) nebo síťová entita podporuje pro komunikační relace. Používá se při vyjednávání relace (např. v SIP nebo SDP) k ustavení spol"
---

LSCS je seznam hlasových a multimediálních kodeků podporovaných uživatelským zařízením nebo síťovou entitou, používaný při vyjednávání relace k ustavení společné sady pro hovor a zajištění interoperability.

## Popis

LSCS (Local Supported Codec Set) je základní koncept při navazování multimediálních relací v IMS a [CS](/mobilnisite/slovnik/cs/) sítích. Představuje úplnou sadu audio, video a dalších mediálních kodeků, které je koncové zařízení (UE) nebo síťový uzel (např. Media Gateway) schopno kódovat a dekódovat. Tato sada je definována lokálně, na základě hardwarových a softwarových schopností zařízení. Při zahájení relace, jako je např. VoLTE hovor nebo videohovor, není LSCS přenášeno přímo. Místo toho slouží jako základ pro sestavení nabídky/odpovědi v protokolu [SDP](/mobilnisite/slovnik/sdp/) (Session Description Protocol).

Proces funguje následovně: Když UE zahájí relaci, využije svůj interní LSCS k vytvoření SDP nabídky. Tato SDP nabídka obsahuje prioritizovaný seznam kodeků z LSCS, které preferuje pro danou relaci. Tento seznam obsahuje u každého kodeku podrobnosti, jako je typ [RTP](/mobilnisite/slovnik/rtp/) payload, vzorkovací frekvence a případné parametry specifické pro daný kodek. Nabídka je odeslána protistraně prostřednictvím signalizace [SIP](/mobilnisite/slovnik/sip/). Přijímající UE porovná nabízený seznam kodeků se svým vlastním LSCS. Následně vygeneruje SDP odpověď, v níž vybere kodek s nejvyšší prioritou, který je zároveň přítomen v jejím lokálně podporovaném souboru.

Toto vzájemné vyjednávání zajišťuje, že oba konce relace používají kodek, který oba podporují, což je klíčové pro interoperabilitu. LSCS je dynamické; může se měnit na základě faktorů, jako jsou aktuální rádiové podmínky (např. UE může vyloučit kodeky s vysokým datovým tokem při špatném pokrytí), nebo omezení služeb ze sítě. Síťové entity jako [P-CSCF](/mobilnisite/slovnik/p-cscf/) nebo [MRFC](/mobilnisite/slovnik/mrfc/) mohou také ovlivnit konečný výběr kodeku na základě síťové politiky, možností překódování nebo správy šířky pásma, případně modifikovat efektivní sadu použitých kodeků oproti původnímu LSCS terminálů.

## K čemu slouží

Koncept LSCS existuje k řešení základního problému mediální interoperability v heterogenních telekomunikačních sítích. Jak se sítě vyvíjely z okruhově přepínaného hlasu (podporujícího jediný, pevný kodek jako [AMR](/mobilnisite/slovnik/amr/)) na paketově přepínaná multimédia (IMS), množství dostupných audio a video kodeků narostlo. Různí výrobci a poskytovatelé služeb začali používat různé kodeky, což vedlo k potenciálním selháním hovorů, pokud koncové body neměly žádný společný podporovaný formát.

LSCS, používané v rámci frameworku [SDP](/mobilnisite/slovnik/sdp/) vyjednávání, poskytuje standardizovaný mechanismus, jak zařízení mohou prezentovat své schopnosti a vzájemně se dohodnout na funkční sadě mediálních kodeků. Tím se řeší omezení statických, předem nakonfigurovaných přiřazení kodeků. Umožňuje to bohaté multimediální služby, zavádění nových, účinnějších kodeků (jako EVS nebo VP9) bez narušení zpětné kompatibility a podporu adaptace kvality tím, že umožňuje výběr kodeku vhodného pro aktuální síťové podmínky a schopnosti zařízení.

## Klíčové vlastnosti

- Definuje vlastní schopnosti kódování/dekódování média pro UE nebo síťový uzel
- Slouží jako zdroj pro sestavování SDP nabídek a odpovědí během vyjednávání relace
- Typicky zahrnuje více kodeků s konfigurovatelnými režimy a datovými toky (např. AMR, AMR-WB, EVS, H.264, H.265)
- Může být dynamicky aktualizováno na základě konfigurace UE, síťové politiky nebo rádiových podmínek
- Nezbytné pro zajištění end-to-end mediální interoperability v IMS a VoLTE
- Používá se spolu se síťovými politikami pro správu šířky pásma a řízení překódování

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [LSCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lscs/)

---
slug: "codec"
url: "/mobilnisite/slovnik/codec/"
type: "slovnik"
title: "CODEC – Coder/Decoder"
date: 2025-01-01
abbr: "CODEC"
fullName: "Coder/Decoder"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/codec/"
summary: "CODEC (kodér/dekodér) je hardwarový nebo softwarový algoritmus, který komprimuje a dekomprimuje digitální mediální datové toky, primárně audio a video. Umožňuje efektivní přenos a uložení snížením obj"
---

CODEC je hardwarový nebo softwarový algoritmus, který komprimuje a dekomprimuje digitální mediální datové toky pro efektivní přenos a uložení v sítích 3GPP, primárně pro hlasové a video služby.

## Popis

CODEC je základní součástí digitálních komunikačních systémů, která plní dvě komplementární funkce: kódování (kompresi) na straně zdroje a dekódování (dekompresi) na straně cíle. Kodér transformuje nezpracovaná digitální mediální data (jako [PCM](/mobilnisite/slovnik/pcm/) audio nebo nezpracované video snímky) do komprimovaného bitového toku odstraněním percepční a statistické redundance. Tato komprese snižuje požadovanou šířku pásma pro přenos nebo kapacitu úložiště. Dekodér na přijímací straně rekonstruuje přibližný obraz původního signálu z komprimovaného bitového toku. Kvalita rekonstrukce závisí na algoritmu CODECu, přenosové rychlosti a inherentním kompromisu mezi kompresním poměrem a věrností.

V systémech 3GPP CODECy fungují v rámci funkcí zpracování médií v uživatelském zařízení (UE) a síťových prvcích, jako je Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo Multimedia Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)). Pro hlasové služby audio subsystém UE zachytí analogový hlas přes mikrofon, převede jej na digitální PCM pomocí [ADC](/mobilnisite/slovnik/adc/) a následně řečový CODEC tento digitální tok komprimuje. Komprimované pakety jsou zabaleny do [RTP](/mobilnisite/slovnik/rtp/)/[UDP](/mobilnisite/slovnik/udp/)/IP rámců pro přenos přes přenosový kanál. V síti může docházet k transkódování mezi různými CODECy (např. mezi [AMR](/mobilnisite/slovnik/amr/) z UE a G.711 z [PSTN](/mobilnisite/slovnik/pstn/)) v Media Gateway. Pro video služby video CODECy zpracovávají video snímky pomocí technik vnitrosnímkové a mezisnímkové komprese, které jsou často standardizovány jak 3GPP, tak externími orgány jako ITU-T nebo MPEG.

Architektura zahrnuje několik klíčových komponent: kompresní algoritmus (např. ACELP pro řeč, DCT a odhad pohybu pro video), mechanismus adaptace přenosové rychlosti, nástroje odolnosti proti chybám a formát přenášených dat pro zabalení do paketů. 3GPP specifikuje nejen algoritmy CODECů, ale také bitově přesnou implementaci, testovací sekvence a povinné podporované profily pro zajištění interoperability. CODECy komunikují s transportní vrstvou prostřednictvím formátů přenášených dat RTP definovaných v IETF RFC a s řídicími protokoly prostřednictvím vyjednávání kodeků v SDP během zřizování relace (např. v SIP nebo SDP).

CODECy hrají klíčovou roli při určování kvality uživatelského zážitku (QoE) a síťové efektivity. Jejich výkon přímo ovlivňuje kvalitu hlasu (měřenou MOS), kvalitu videa, spotřebu šířky pásma, latenci a odolnost proti chybám. Pokročilé CODECy obsahují funkce jako detekce hlasové aktivity (VAD) pro nespojitý přenos, generování komfortního šumu (CNG), maskování ztráty paketů (PLC) a adaptivní více rychlostní provoz, který dynamicky upravuje přenosovou rychlost na základě síťových podmínek. V systémech 5G CODECy umožňují pohlcující mediální služby jako VR/AR a ultra-HD video díky vyšší kompresní účinnosti a nižší latenci.

## K čemu slouží

CODECy existují, aby řešily základní problém omezené přenosové kapacity a kapacity úložiště v digitálních komunikačních systémech. Nezpracovaná digitální média vyžadují značné datové toky – například nekomprimované audio ve kvalitě CD (44,1 kHz, 16bitové stereo) potřebuje přibližně 1,4 Mbps, zatímco nezpracované HD video může vyžadovat přes 1 Gbps. Přenos takových objemů přes omezená bezdrátová spojení, jako jsou mobilní sítě, by byl nepraktický a ekonomicky neproveditelný. CODECy umožňují praktické multimediální služby komprimací dat 10 až 1000krát, čímž se služby jako hlasové hovory, streamování videa a konferenční hovory stávají realizovatelnými přes mobilní sítě.

Historicky přechod z analogové na digitální mobilní síť (2G GSM) vytvořil potřebu efektivního digitálního kódování řeči. Rané mobilní sítě používaly řečové kodeky s plnou rychlostí a relativně vysokými přenosovými rychlostmi (13 kbps pro GSM FR). Jak se sítě vyvíjely, aby podporovaly více uživatelů a datové služby, byly vyvíjeny pokročilejší kodeky s nižšími přenosovými rychlostmi a lepší kvalitou. Každá generace přinesla vylepšené kodeky: 3G zavedlo AMR s adaptivními rychlostmi, 4G přineslo HD hlas s AMR-WB a 5G podporuje ještě účinnější kodeky jako EVS a vylepšené video kodeky. Tento vývoj řešil omezení předchozích kodeků z hlediska efektivity využití šířky pásma, kvality hlasu, odolnosti vůči ztrátě paketů a podpory nových audio šířek pásma (jako širokopásmové a super-širokopásmové).

Kromě základní komprese moderní kodeky řeší další problémy: umožňují interoperabilitu mezi různými sítěmi (mobilní, VoIP, PSTN) prostřednictvím transkódování, podporují adaptaci kvality na měnící se síťové podmínky prostřednictvím více rychlostního provozu a poskytují odolnost proti chybám pro nespolehlivé bezdrátové kanály. Také umožňují nové služby, jako jsou konference více účastníků, streamování hudby a pohlcující média, tím, že nabízejí vhodné kompresní profily pro různé typy obsahu. Bez efektivních kodeků by bohatý multimediální ekosystém dnešních mobilních sítí neexistoval.

## Klíčové vlastnosti

- Ztrátové kompresní algoritmy optimalizované pro lidské vnímání
- Více rychlostní provoz podporující dynamickou adaptaci přenosové rychlosti
- Mechanismy odolnosti proti chybám včetně maskování ztráty paketů
- Podpora více audio šířek pásma (od úzkopásmové po super-širokopásmovou)
- Standardizované bitově přesné implementace zajišťující interoperabilitu
- Integrace s RTP/IP transportem prostřednictvím definovaných formátů přenášených dat

## Definující specifikace

- **TS 22.233** (Rel-19) — Packet-switched Streaming Service (PSS) Stage 1
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TR 26.916** (Rel-14) — eSRVCC Transcoding Minimization Study

---

📖 **Anglický originál a plná specifikace:** [CODEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/codec/)

---
slug: "cs-mgw"
url: "/mobilnisite/slovnik/cs-mgw/"
type: "slovnik"
title: "CS-MGW – Circuit Switched Media Gateway"
date: 2025-01-01
abbr: "CS-MGW"
fullName: "Circuit Switched Media Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cs-mgw/"
summary: "CS-MGW je síťový prvek, který provádí mediální konverzi a překódování mezi sítěmi s přepojováním okruhů (CS) (jako PSTN/ISDN) a sítěmi s přepojováním paketů (PS) (jako IP v 3GPP). Umožňuje služby hlas"
---

CS-MGW je síťový prvek, který provádí mediální konverzi a překódování mezi sítěmi s přepojováním okruhů, jako je PSTN, a paketovými IP sítěmi, aby umožnil služby hlasu a dat CS přes IP přenos.

## Popis

Circuit Switched Media Gateway (CS-MGW) je klíčová funkční entita v jádrové síti 3GPP, konkrétně v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Slouží jako most mezi tradičními sítěmi s přepojováním okruhů založenými na časovém multiplexu ([TDM](/mobilnisite/slovnik/tdm/)), jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) a síť [ISDN](/mobilnisite/slovnik/isdn/), a sítěmi s přepojováním paketů založenými na protokolu IP nebo režimu [ATM](/mobilnisite/slovnik/atm/). Architektonicky je CS-MGW řízen funkcí Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) prostřednictvím protokolu H.248 (Megaco), který je v 3GPP standardizován jako rozhraní Mn. MGCF poskytuje řízení hovoru a signalizační inteligenci, zatímco CS-MGW provádí operace v uživatelské rovině médií podle příkazů. Toto oddělení řídicí a uživatelské roviny je základním principem architektury řízení bran přijaté 3GPP.

Z funkčního hlediska je primární úlohou CS-MGW zpracování médií. Ukončuje přenosové kanály ze sítě CS (např. E1/T1 trunky s TDM časovými sloty) a mediální toky ze sítě [PS](/mobilnisite/slovnik/ps/) (např. toky protokolu [RTP](/mobilnisite/slovnik/rtp/) přes IP). Jeho základní operace zahrnují mediální konverzi, překódování a zpracování přenosu. Mediální konverze zahrnuje adaptaci přenosového formátu, například převod 64 kbps PCM hlasového kanálu z TDM okruhu na paketový tok RTP/UDP/IP pro přenos přes IP síť a naopak. Překódování je proces konverze mezi různými řečovými kodeky, což je nezbytné, když se kodek používaný v mobilní síti (např. AMR) liší od kodeku používaného ve fixní síti (např. G.711). CS-MGW může také provádět potlačení echa, generování tónů (např. oznamovacího tónu, tónu obsazeno) a konferenční funkce pro hovory více účastníků.

CS-MGW má rozhraní k několika dalším síťovým prvkům. Na straně CS se připojuje k legacy síti s přepojováním okruhů přes TDM rozhraní. Uvnitř IMS nebo CS jádra 3GPP se připojuje k MGCF pro řízení (rozhraní Mn) a k dalším mediálním branám nebo koncovým bodům pro provoz v uživatelské rovině. V kontextu architektury založené na MSC serveru, zavedené ve 3GPP Release 4, je CS-MGW koncovým bodem uživatelské roviny, který je řízen MSC serverem. To umožňuje rozdělení tradičního monolitického MSC na server řízení hovorů (MSC Server) a entitu zpracování médií (CS-MGW), což umožňuje flexibilnější a škálovatelnější nasazení sítí. CS-MGW je tedy klíčovým prvkem pro modernizaci sítí, který operátorům umožňuje migrovat svou hlasovou infrastrukturu na plně IP páteřní sítě při zachování interoperability s legacy službami a sítěmi s přepojováním okruhů.

## K čemu slouží

CS-MGW byl vytvořen, aby řešil základní výzvu konvergence sítí mezi legacy telefonními sítěmi s přepojováním okruhů a vznikajícími sítěmi s přepojováním paketů. Před jeho zavedením byly hlasové služby poskytovány výhradně přes vyhrazené TDM okruhy, které jsou efektivní pro hlas s konstantní přenosovou rychlostí, ale pro přenos dat jsou nepružné a nákladné. Vzestup IP jako univerzálního síťového protokolu představoval příležitost přenášet hlas jako paketizovaná data, což nabízí statistické multiplexní zisky, zjednodušenou infrastrukturu a potenciál pro integrované multimediální služby. Byl však zapotřebí přímý most pro propojení těchto dvou odlišných technologických světů bez narušení stávajících služeb.

Primární problém, který CS-MGW řeší, je vzájemné propojení přenosového provozu a základních funkcí hovoru mezi doménami TDM a IP/ATM. Umožňuje operátorům mobilních sítí modernizovat jejich jádrové sítě nasazením IP přenosu a řízení (např. pomocí MSC serverů) při zachování připojení ke globální PSTN/ISDN, která po mnoho let zůstávala převážně TDM. Tento přechod byl ekonomicky motivovaný, protože IP sítě jsou obecně levnější na výstavbu, údržbu a škálování. CS-MGW pod řízením MGCF nebo MSC serveru zvládá komplexní zpracování médií v reálném čase potřebné pro toto vzájemné propojení, čímž izoluje logiku řízení hovoru od specifik podkladové přenosové technologie. Jeho vytvoření bylo klíčovým krokem v evoluci směrem k plně IP jádrovým sítím a bylo základní komponentou pro pozdější zavedení IMS pro multimediální služby.

## Klíčové vlastnosti

- Mediální konverze mezi TDM okruhy a paketovými toky IP/ATM
- Překódování řečových kodeků (např. mezi AMR a G.711)
- Potlačení echa a generování/oznamování tónů
- Ukončení a zpracování přenosu pod řízením H.248 (Megaco)
- Podpora pro přenos DTMF v pásmu i mimo pásmo
- Rozhraní s MGCF (Mn) a legacy CS sítěmi (např. přes E1/T1)

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [CS-MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/cs-mgw/)

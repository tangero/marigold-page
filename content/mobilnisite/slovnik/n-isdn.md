---
slug: "n-isdn"
url: "/mobilnisite/slovnik/n-isdn/"
type: "slovnik"
title: "N-ISDN – Narrowband Integrated Services Digital Network"
date: 2002-01-01
abbr: "N-ISDN"
fullName: "Narrowband Integrated Services Digital Network"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/n-isdn/"
summary: "Narrowband ISDN (N-ISDN) je přepojování okruhů využívající standard digitální telekomunikace poskytující integrované hlasové a datové služby přes tradiční měděné telefonní linky. Šlo o základní techno"
---

N-ISDN je přepojování okruhů využívající standard digitální telekomunikace, který poskytuje integrované hlasové a datové služby přes tradiční měděné telefonní linky.

## Popis

Narrowband Integrated Services Digital Network (N-ISDN) je soubor komunikačních standardů definovaných [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatých v rámci 3GPP pro digitální přenos hlasu, videa a dat přes tradiční telefonní síť s přepojováním okruhů. Funguje přes stávající měděné telefonní linky, ale používá digitální signalizaci a přenos, čímž nabízí vyšší kvalitu a více funkcí než analogové systémy. Architektura je založena na dvou základních typech kanálů: přenosové (B) kanály pro uživatelská data a signalizační (D) kanály pro signalizaci a řízení. Mezi běžné struktury rozhraní patří základní přístupové rozhraní ([BRI](/mobilnisite/slovnik/bri/)), které nabízí 2 B kanály (64 kbps každý) a 1 D kanál (16 kbps), a primární přístupové rozhraní (PRI), které nabízí 23 B kanálů a 1 D kanál (v Severní Americe) nebo 30 B kanálů a 1 D kanál (v Evropě).

V kontextu 3GPP se na N-ISDN odkazuje především kvůli provozu se staršími sítěmi a definicím služeb. Představuje specifickou třídu externích sítí, ke kterým se může mobilní síť jádra, například jádrová síť GSM nebo UMTS, připojit pro služby s přepojováním okruhů. Samotná síť N-ISDN není součástí architektury definované 3GPP, ale je považována za koncový bod pro hovory a datové relace. Ústředna mobilního přepojování ([MSC](/mobilnisite/slovnik/msc/)) v síti jádra by zajišťovala potřebnou protokolovou konverzi a funkce pro provoz s jinou sítí ([IWF](/mobilnisite/slovnik/iwf/)) pro komunikaci se sítí N-ISDN.

Její role je historická, ale významná, neboť stanovila princip integrovaných digitálních služeb. Signalizační protokoly používané v N-ISDN, zejména řada Q.931 pro řízení hovorů, ovlivnily vývoj signalizace v mobilních sítích. Přestože je pro nová nasazení z velké části zastaralá, porozumění N-ISDN je důležité pro pochopení vývoje od sítí jádra s přepojováním okruhů k sítím s přepojováním paketů (IP) a starších systémů, se kterými byly sítě 3GPP navrženy pro interoperabilitu.

## K čemu slouží

N-ISDN byl vytvořen za účelem modernizace globální telefonní sítě přechodem z analogové na digitální technologii, čímž se zlepšila kvalita hlasu, zkrátil čas potřebný pro sestavení hovorů a umožnily nové datové služby přes stejnou měděnou infrastrukturu. Vyřešil problém existence samostatných sítí pro hlas a nízkorychlostní data jejich integrací do jediné digitální sítě. Historickým kontextem byla snaha konce 20. století o plně digitální 'Integrated Services Digital Network' ([ISDN](/mobilnisite/slovnik/isdn/)), přičemž N-ISDN představoval počáteční úzkopásmovou implementaci cílenou na široký spotřebitelský a podnikový přístup.

Omezení, která řešil, byla vlastní analogové veřejné telefonní síti (PSTN), která byla náchylná k šumu, podporovala pouze data v hlasovém pásmu při velmi nízkých rychlostech (pomocí modemů) a vyžadovala samostatné linky pro různé služby. N-ISDN poskytoval nezabrané digitální okruhy 64 kbps, rychlejší sestavení hovoru pomocí mimopásmové signalizace na D-kanálu a možnost podpory současného hlasu a dat na stejné lince. Jeho zahrnutí do standardů 3GPP zajišťovalo, že se rané mobilní sítě 2G a 3G mohly bezproblémově připojovat a poskytovat služby kompatibilní s převažujícími pevnými digitálními sítěmi své doby, což usnadňovalo univerzální konektivitu.

## Klíčové vlastnosti

- Digitální přenos s přepojováním okruhů
- Integrované hlasové a datové služby na jedné přístupové lince
- Základní přístupové rozhraní (2B+D) a primární přístupové rozhraní (23B+D/30B+D)
- Mimopásmová signalizace využívající samostatný D-kanál
- Standardizovaný protokol pro řízení hovorů Q.931
- Provoz s legacy analogovou PSTN a pozdějšími paketovými sítěmi

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements

---

📖 **Anglický originál a plná specifikace:** [N-ISDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-isdn/)

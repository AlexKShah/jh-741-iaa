library(ggplot2)

create_histograms <- function(file_path, site_name, host_ip = "10.0.2.15") {
  # Read the CSV
  df <- read.csv(file_path, header = TRUE, stringsAsFactors = FALSE)
  
  # Clean column names and convert packet length
  names(df) <- gsub("\\.", "", names(df))
  colnames(df)[colnames(df) == "Length"] <- "PacketLength"
  df$PacketLength <- as.numeric(df$PacketLength)
  
  # Separate outgoing and incoming packets
  outgoing <- subset(df, Source == host_ip)
  incoming <- subset(df, Destination == host_ip)
  
  # Create outgoing plot
  p_out <- ggplot(outgoing, aes(x = PacketLength)) +
    geom_histogram(binwidth = 50, fill = "skyblue", color = "black") +
    labs(
      title = paste("Outgoing Packet Sizes to", site_name),
      x = "Packet Size (bytes)",
      y = "Number of Packets"
    ) +
    theme_minimal() +
    theme(panel.grid = element_blank())
  
  # Create incoming plot
  p_in <- ggplot(incoming, aes(x = PacketLength)) +
    geom_histogram(binwidth = 50, fill = "seagreen", color = "black") +
    labs(
      title = paste("Incoming Packet Sizes from", site_name),
      x = "Packet Size (bytes)",
      y = "Number of Packets"
    ) +
    theme_minimal() +
    theme(panel.grid = element_blank())
  
  # Save plots to PNG files in working directory
  ggsave(paste0(site_name, "_out.png"), plot = p_out, width = 8, height = 6, dpi = 300)
  ggsave(paste0(site_name, "_in.png"), plot = p_in, width = 8, height = 6, dpi = 300)
}

# Run the function for each site's CSV
create_histograms("cnnweb.csv", "CNN")
create_histograms("aleaeweb.csv", "ALEAE")
create_histograms("amazonweb.csv", "Amazon")
create_histograms("foxweb.csv", "FOX")

